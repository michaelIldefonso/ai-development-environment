from orchestrator.state import ProjectState


def planner(state: ProjectState):
    task = state["task"]

    return {
        "plan": f"Proposed plan for: {task}"
    }