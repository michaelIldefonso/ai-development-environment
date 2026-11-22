
from orchestrator.state import ProjectState
from adaptors.gemini import model
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field


class TesterOutput(BaseModel):
    test_passed: bool = Field(
        description="Whether the implementation passes the evaluation."
    )

    test_feedback: str = Field(
        description="Explanation of the evaluation results and identified issues."
    )


structured_model = model.with_structured_output(TesterOutput)


tester_prompt = ChatPromptTemplate.from_messages([
    ("system", """
    You are a software testing and quality assurance engineer.

    Evaluate the implementation against the task, requirements, and development plan.

    Identify missing features, incorrect behavior, and implementation problems.

    Do not automatically approve incomplete implementations.
    """),
    ("human", """
    Task:
    {task}

    Requirements:
    {requirements}

    Plan:
    {plan}

    Code:
    {code}
    """)
])


def tester(state: ProjectState):

    prompt = tester_prompt.format(
        task=state["task"],
        requirements=state["requirements"],
        plan=state["plan"],
        code=state["code"]
    )

    response = structured_model.invoke(prompt)

 # Calculate retry count
    new_retry_count = (
        state["retry_count"] + 1
        if not response.test_passed
        else state["retry_count"]
    )

    # Log evaluation
    print("\n========== TESTER ==========")
    print("Passed:", response.test_passed)
    print("Feedback:", response.test_feedback)
    print(
        f"Retry count: {state['retry_count']} -> {new_retry_count}"
    )


    return {
        "test_passed": response.test_passed,
        "test_feedback": response.test_feedback,
        "retry_count": new_retry_count
    }



