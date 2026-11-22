
from langgraph.graph import END
from orchestrator.state import ProjectState


def decide_next(state: ProjectState):
    if state["needs_research"]:
        return "researcher"

    return "developer"


def decide_after_test(state: ProjectState):
    if state["test_passed"]:
        return "reviewer"

    if state["retry_count"] < 3:
        return "developer"

    return "human_intervention"


def decide_after_review(state: ProjectState):
    if state["review_passed"]:
        return END

    if state["retry_count"] < 3:
        return "developer"

    return "human_intervention"
