from typing import TypedDict


class ProjectState(TypedDict):
    # Task information
    task: str
    requirements: str

    # Planning and research
    plan: str
    research: str
    needs_research: bool #un needed, can be removed in future

    # Development
    code: str
    human_feedback: str

    # Testing and retries
    retry_count: int
    test_passed: bool
    test_feedback: str

    #review
    review_passed: bool
    review_feedback: str
    # Human interaction
    human_response: str #redundant, can be removed in future