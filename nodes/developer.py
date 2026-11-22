from orchestrator.state import ProjectState
from adaptors.gemini import model
from langchain_core.prompts import ChatPromptTemplate

developer_prompt = ChatPromptTemplate.from_messages([
    ("system", """
    You are a software development developer.
    Implement the requested solution based on the task, requirements, plan, and research.

    Output ONLY the source code.
    Do not include explanations, introductions, conclusions, or Markdown code fences.
    """),
    ("human", """
    Previous implementation:
    {code}

    Tester feedback:
    {test_feedback}

    Task:
    {task}

    Requirements:
    {requirements}

    Plan:
    {plan}

    Research:
    {research}
    """)
])


def developer(state: ProjectState):

    print("\n========== DEVELOPER ==========")
    print("Starting implementation...")
    print("Retry count:", state["retry_count"])
    print("Human feedback:", state["human_feedback"])
    print("Previous tester feedback:", state["test_feedback"])
    print("Previous reviewer feedback:", state["review_feedback"])

    prompt = developer_prompt.format(
        task=state["task"],
        requirements=state["requirements"],
        plan=state["plan"],
        research=state["research"],
        code=state["code"],
        test_feedback=state["test_feedback"]
    )

    response = model.invoke(prompt)

    print("[DEVELOPER] Implementation generated successfully.")
    print("[DEVELOPER] Generated code:")
    print(response.text)

    return {"code": response.text}
