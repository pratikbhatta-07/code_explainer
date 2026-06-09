from src.services.groq_services import get_groq_client

client = get_groq_client()


def generate_tests(code: str, language: str) -> str:

    system_prompt = """
            You are an expert software engineer and testing specialist.
            Analyze the given code and generate meaningful unit tests.

            Instructions:
            1. Identify the programming language.
            2. Understand the function or method behavior.
            3. Generate comprehensive unit tests.
            4. Cover :
                - Normal cases
                - Edge cases
                - Boundary cases
                - Invalid inputs (if applicable)
            5. Use the standard testing framework for the language:
                - Java → JUnit
                - Python → unittest or pytest
                - JavaScript → Jest
                - C++ → Google Test
            6. Output only the test code with brief explanations.

            Output Format :
            Language:
            Testing Framework:
            Generated Tests:
            Test Coverage Summary:
            """

    user_prompt = f"""
Programming Language: {language}

Generate unit tests for the following code:

```{language}
{code}"""