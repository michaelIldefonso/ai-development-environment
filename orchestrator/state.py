from typing import TypedDict, Literal


class ProjectState(TypedDict):
    # User input
    task: str
    mode: Literal["developer_led", "ai_assisted"]

    # Worker outputs
    plan: str
    research: str
    code_changes: str
    test_results: str
    review: str

    # Workflow decisions
    tests_passed: bool
    review_approved: bool
    human_approved: bool

    # Workflow control
    retry_count: int
    messages: list[str]