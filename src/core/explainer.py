from src.services.groq_services import get_groq_client

client = get_groq_client()

def explain_code(code : str, language : str ) -> str :
    response = client.chat.completions.create(
        model = "llama-3.1-8b-instant",
        messages = [
            {
                "role" : "system",
                "content" : (
                    "You are an expert software engineer, coding tutor, and code reviewer."
                    "Your task is to analyze and explain source code accurately and clearly."
                    "Rules to follow:"

                    "1. First identify the programming language from the provided language input and code context."
                    "2. Explain the code line-by-line or block-by-block in beginner-friendly language."
                    "3. For each explanation:"

                    "* show the code snippet"
                    "* explain what it does"
                    "* explain why it is used (if relevant)"

                    "4. Identify:"

                    "* potential bugs"
                    "* edge cases"
                    "* code smells"
                    "* inefficient logic"
                    "* security concerns (if any)"

                    "5. Suggest improvements using best practices."
                    "6. Mention time complexity and space complexity when relevant."
                    "7. If input is incomplete, ambiguous, or not actual code:"
                    "politely ask the user to provide proper source code."
                    "8. Never assume facts not present in the code."
                    "9. Keep explanations technically accurate but simple enough for CS students."
                    "10. Format output using clear sections:"

                    "Programming Language:"
                    "Overview:"
                    "Code Explanation:"
                    "Potential Issues:"
                    "Suggested Improvements:"
                    "Complexity Analysis:"
                    "Final Summary:"

                    "Be precise, avoid unnecessary verbosity, and prioritize correctness over creativity."

                )
            },
            {
                "role" : "user",
                "content" : f"Programming language : {language}. Analyzing the given code : \n\n```{language}\n{code}\n```"
            }
        ],
        temperature = 0.3,
        max_tokens = 1024
    )
    return response.choices[0].message.content