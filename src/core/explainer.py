from src.services.groq_services import get_groq_client

client = get_groq_client()

def explain_code(java_code : str) -> str :
    response = client.chat.completions.create(
        model = "llama-3.1-8b-instant",
        messages = [
            {
                "role" : "system",
                "content" : (
                    "You are an expert Java developer and patient teacher. "
                    "When given Java code, explain EACH LINE in simple terms "
                    "that a CS student would understand. "
                    "Format: show the code line, then explain it in one sentence. "
                    "Highlight any design patterns, potential bugs, or best practices."
                )
            },
            {
                "role" : "user",
                "content" : f"Please explain this java code : \n\n```java\n{java_code}\n```"
            }
        ],
        temperature = 0.3,
        max_tokens = 1024
    )
    return response.choices[0].message.content