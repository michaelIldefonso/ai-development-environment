from orchestrator.state import ProjectState
from orchestrator.routing import decide_next, decide_after_test, decide_after_review

from nodes import (
    developer,
    planner,
    tester,
    researcher,
    human_intervention,
    human_input,
    reviewer
)

from langgraph.graph import StateGraph, START
from langgraph.checkpoint.memory import InMemorySaver

builder = StateGraph(ProjectState)

# Register nodes
builder.add_node("planner", planner)
builder.add_node("researcher", researcher)
builder.add_node("developer", developer)
builder.add_node("tester", tester)
builder.add_node("human_intervention", human_intervention)
builder.add_node("human_input", human_input)
builder.add_node("reviewer", reviewer)


# Define execution flow
builder.add_edge(START, "human_input")
builder.add_edge("human_input", "planner")

builder.add_conditional_edges("planner", decide_next)

builder.add_edge("researcher", "developer")
builder.add_edge("developer", "tester")

builder.add_conditional_edges("tester", decide_after_test)
builder.add_edge("human_intervention", "developer")
builder.add_conditional_edges("reviewer", decide_after_review)

checkpointer = InMemorySaver()

graph = builder.compile(checkpointer=checkpointer)