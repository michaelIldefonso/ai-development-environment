from orchestrator.state import ProjectState
from adaptors.gemini import model
from langchain_core.prompts import ChatPromptTemplate

researcher_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a software development researcher. Gather and analyze information."),
    ("human", """
    Task:
    {task}

    Requirements:
    {requirements}

    Plan:
    {plan}
    """)
])


def researcher(state: ProjectState):

    print("\n========== RESEARCHER ==========")
    print("Task:", state["task"])
    print("Requirements:", state["requirements"])
    print("Plan:", state["plan"])
    print("[RESEARCHER] Gathering research...")

    prompt = researcher_prompt.format(
        task=state["task"],
        requirements=state["requirements"],
        plan=state["plan"]
    )

    response = model.invoke(prompt)

    print("[RESEARCHER] Research completed successfully.")
    print("Research output:")
    print(response.text)

    return {"research": response.text}
