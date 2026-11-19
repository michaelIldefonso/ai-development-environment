from orchestrator.state import ProjectState


def reviewer(state: ProjectState):
    plan = state["plan"]
    tests_passed = state["tests_passed"]

    # Temporary mock review decision
    review_approved = False

    return {
        "review": (
            f"Reviewing plan: {plan}\n"
            f"Tests passed: {tests_passed}"
        ),
        "review_approved": review_approved
    }