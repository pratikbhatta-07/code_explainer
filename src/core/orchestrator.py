from src.tools.complexity_tool import analyze_complexity
from src.tools.explanation_tool import explain_code
from src.tools.test_tool import generate_tests

def full_review(code : str, language : str) -> str :
    explanation = explain_code(code, language, "interview")
    complexity = analyze_complexity(code)
    tests = generate_tests(code, language)
    report = f""" 
            Full Review Report : {explanation}
            Complexity Analysis : {complexity}
            Test Cases : {tests}
            """
    return report