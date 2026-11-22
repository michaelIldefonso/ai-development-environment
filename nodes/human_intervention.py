from orchestrator.state import ProjectState
from langgraph.types import interrupt

def human_intervention(state: ProjectState):
    print("Retry count before HITL:", state["retry_count"])

    response = interrupt({
        "message": (
            f"QA failed after {state['retry_count']} attempts.\n\n"
            f"Tester result: {state['test_passed']}\n"
            f"Tester feedback: {state['test_feedback']}\n\n"
            f"Reviewer result: {state['review_passed']}\n"
            f"Reviewer feedback: {state['review_feedback']}\n\n"
            "What should the Developer try next?"
        )
    })

    return {
        "human_feedback": response,
        "retry_count": 0
    }