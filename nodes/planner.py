from orchestrator.state import ProjectState
from adaptors.gemini import model
from langchain_core.prompts import ChatPromptTemplate

planner_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a software development planner. Create clear, practical development plans."),
    ("human", """
    Task:
    {task}

    Requirements:
    {requirements}
    """)
])


def planner(state: ProjectState):

    print("\n========== PLANNER ==========")
    print("Task:", state["task"])
    print("Requirements:", state["requirements"])
    print("[PLANNER] Generating development plan...")

    prompt = planner_prompt.format(
        task=state["task"],
        requirements=state["requirements"]
    )

    response = model.invoke(prompt)

    print("[PLANNER] Plan generated successfully.")
    print("Generated plan:")
    print(response.text)

    return {"plan": response.text}
