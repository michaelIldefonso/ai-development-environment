from langgraph.types import Command
from workflows.ai_assisted import graph


config = {
    "configurable": {
        "thread_id": "project-001"
    }
}

initial_state = {
    "task": "",
    "requirements": "",
    "plan": "",
    "research": "",
    "code": "",
    "human_response": "", #redundant, can be removed in future
    "human_feedback": "",
    "test_feedback": "",
    "review_feedback": "",
    "retry_count": 0,
    "needs_research": True, #un needed, can be removed in future
    "test_passed": False,
    "review_passed": False,
}
result = graph.invoke(initial_state, config)

while result.get("__interrupt__"):
    interrupt_data = result["__interrupt__"][0].value

    print(interrupt_data)

    if "question" in interrupt_data:
        task = input("Task: ")
        requirements = input("Requirements: ")

        response = {
            "task": task,
            "requirements": requirements
        }

    else:
        print(interrupt_data["message"])
        response = input("Your guidance: ")
        
    result = graph.invoke(
        Command(resume=response),
        config
    )

print(result)