from orchestrator.state import ProjectState
from langgraph.types import interrupt

def human_input(state: ProjectState):
    response = interrupt({
        "question": "Describe the task and its requirements."
    })

    return {
        "task": response["task"],
        "requirements": response["requirements"]
    }