
from orchestrator.state import ProjectState
from adaptors.gemini import model
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field


class ReviewerOutput(BaseModel):
    review_passed: bool = Field(
        description="Whether the implementation meets the code quality and architectural expectations."
    )

    review_feedback: str = Field(
        description="Explanation of identified code quality issues or approval."
    )


structured_model = model.with_structured_output(ReviewerOutput)


reviewer_prompt = ChatPromptTemplate.from_messages([
    ("system", """
    You are an experienced software engineer performing an independent code review.

    Review the implementation for:
    - Code quality and readability.
    - Maintainability.
    - Architectural consistency.
    - Potential bugs and logical errors.
    - Compliance with the task and requirements.

    Do not automatically approve incomplete or poorly implemented code.

    Do not rewrite the implementation.
    Provide actionable feedback.
    """),
    ("human", """
    Task:
    {task}

    Requirements:
    {requirements}

    Plan:
    {plan}

    Research:
    {research}

    Implementation:
    {code}

    Testing feedback:
    {test_feedback}
    """)
])


def reviewer(state: ProjectState):

    prompt = reviewer_prompt.format(
        task=state["task"],
        requirements=state["requirements"],
        plan=state["plan"],
        research=state["research"],
        code=state["code"],
        test_feedback=state["test_feedback"]
    )

    response = structured_model.invoke(prompt)

    # Calculate retry count
    new_retry_count = (
        state["retry_count"] + 1
        if not response.review_passed
        else 0
    )

    # Log evaluation
    print("\n========== REVIEWER ==========")
    print("Passed:", response.review_passed)
    print("Feedback:", response.review_feedback)
    print(
        f"Retry count: {state['retry_count']} -> {new_retry_count}"
    )

    return {
        "retry_count": new_retry_count,
        "review_passed": response.review_passed,
        "review_feedback": response.review_feedback
    }