from orchestrator.state import ProjectState


def developer(state: ProjectState):
    task = state["task"]
    feedback = state["review"]
    retry_count = state["retry_count"] + 1

    return {
        "code_changes": (
            f"Implementation attempt {retry_count} for: {task}\n"
            f"Addressing review feedback: {feedback}"
        ),
        "retry_count": retry_count
    }
