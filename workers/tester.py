from orchestrator.state import ProjectState


def tester(state: ProjectState):
    code_changes = state["code_changes"]

    # Temporary mock test result
    tests_passed = True

    return {
        "test_results": (
            f"Testing implementation:\n{code_changes}\n"
            f"Tests passed: {tests_passed}"
        ),
        "tests_passed": tests_passed
    }