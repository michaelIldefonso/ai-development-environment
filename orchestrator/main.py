
from langgraph.graph import StateGraph, START, END
from orchestrator.state import ProjectState


from workers.planner import planner
from workers.reviewer import reviewer
from orchestrator.routing import review_router
from workers.developer import developer
from workers.tester import tester
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import Command
from workers.human_approval import human_approval

# Build graph
builder = StateGraph(ProjectState)

builder.add_node("planner", planner)
builder.add_node("developer", developer)
builder.add_node("reviewer", reviewer)
builder.add_node("tester", tester)
builder.add_node("human_approval", human_approval)

builder.add_edge(START, "planner")
builder.add_edge("planner", "developer")
builder.add_edge("developer", "tester")
builder.add_edge("tester", "reviewer")

builder.add_conditional_edges(
    "reviewer",
    review_router,
    {
        "test_failed": "developer",
        "review_rejected": "developer",
        "human_review": "human_approval"
    }
)

builder.add_edge("human_approval", END)

checkpointer = InMemorySaver()
graph = builder.compile(checkpointer=checkpointer)

# Execute graph
config = {
    "configurable": {
        "thread_id": "music-player-task-001"
    }
}

initial_state = {
    "task": "Build a music player application",
    "mode": "ai_assisted",
    "plan": "",
    "research": "",
    "code_changes": "",
    "test_results": "",
    "review": "",
    "tests_passed": False,
    "review_approved": False,
    "human_approved": False,
    "retry_count": 0,
    "messages": []
}

result = graph.invoke(initial_state, config=config)

# Check whether the workflow paused for approval
interrupts = result.get("__interrupt__", [])

if interrupts:
    approval_request = interrupts[0].value

    print("\n=== HUMAN APPROVAL REQUIRED ===")
    print("Task:", approval_request["task"])
    print("\nPlan:", approval_request["plan"])
    print("\nImplementation:", approval_request["code_changes"])
    print("\nTest Results:", approval_request["test_results"])
    print("\nReview:", approval_request["review"])

    decision = input("\nApprove implementation? (y/n): ").strip().lower()

    approved = decision in ("y", "yes")

    result = graph.invoke(
        Command(resume=approved),
        config=config
    )

print("\n=== WORKFLOW FINISHED ===")
print(result)