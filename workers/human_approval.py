from langgraph.types import interrupt
from orchestrator.state import ProjectState


def human_approval(state: ProjectState):
    decision = interrupt({
        "message": "The AI workflow is awaiting human approval.",
        "task": state["task"],
        "plan": state["plan"],
        "code_changes": state["code_changes"],
        "test_results": state["test_results"],
        "review": state["review"]
    })

    return {
        "human_approved": decision
    }