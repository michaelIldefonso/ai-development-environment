from orchestrator.state import ProjectState

MAX_RETRIES = 3


def review_router(state: ProjectState):
    if not state["tests_passed"]:
        if state["retry_count"] < MAX_RETRIES:
            return "test_failed"
        return "human_review"

    if not state["review_approved"]:
        if state["retry_count"] < MAX_RETRIES:
            return "review_rejected"
        return "human_review"

    return "human_review"