from src.services.groq_services import get_groq_client

client = get_groq_client()

def explain_code(code : str, language : str, mode : str ) -> str :

    prompts = {
        "beginner" : ("""You are an expert software engineer and a patient coding tutor.

                                Your goal is to help beginners understand code clearly and confidently.

                                Instructions:
                                1. First identify the programming language.
                                2. Provide a short overview of what the program does.
                                3. Explain the code line-by-line or block-by-block in simple language.
                                4. Avoid unnecessary technical jargon.
                                5. When introducing a technical concept, explain it in beginner-friendly terms.
                                6. Use simple real-world analogies whenever helpful.
                                7. Explain WHY a statement is used, not just WHAT it does.
                                8. Highlight important programming concepts such as loops, functions, recursion,classes, arrays, hash maps, etc.
                                9. Mention common beginner mistakes related to the code if relevant.
                                10. If the code contains bugs, explain them gently and suggest fixes.

                                Output Format:
                                Programming Language:
                                Program Overview:
                                Code Explanation:
                                Key Concepts Learned:
                                Potential Issues:
                                Summary:

                                Prioritize clarity and teaching over brevity.
                                Assume the reader is a CS student who is still learning programming."""
                                ),

        "interview" : ("""You are a senior software engineer conducting a technical interview.

                                Your task is to analyze the code as an interviewer would.

                                Instructions:
                                1. Identify the programming language.
                                2. Give a concise explanation of the solution approach.
                                3. Explain the core logic and reasoning behind the implementation.
                                4. Identify the data structures and algorithms being used.
                                5. Calculate and explain:

                                * Time Complexity
                                * Space Complexity

                                6. Point out edge cases the code may fail on.
                                7. Suggest optimizations if possible.
                                8. Mention tradeoffs between the current solution and alternative approaches.
                                9. Identify any code quality concerns.
                                10. Generate 3-5 realistic interviewer follow-up questions related to the code.

                                Output Format:
                                Programming Language:
                                Solution Approach:
                                Logic Breakdown:
                                Data Structures & Algorithms:
                                Time Complexity:
                                Space Complexity:
                                Edge Cases:
                                Possible Optimizations:
                                Code Review:
                                Interviewer Follow-Up Questions:

                                Be concise, analytical, and technically rigorous.
                                Focus on interview preparation rather than teaching beginners."""
                            ),
 
    }

    system_prompt = prompts.get(mode, ("You are an expert software engineer. Explain the code clearly, identify potential issues, and provide accurate technical insights."))

    user_prompt = f"""Programming Language : {language}
      Analyse the following code : 
      ```{language} {code}"""


    try :
        response = client.chat.completions.create(
            model = "llama-3.1-8b-instant",
            messages = [
                {
                    "role" : "system",
                    "content" : system_prompt
                },
                {
                    "role" : "user",
                    "content" : user_prompt
                }
            ],
            temperature = 0.3,
            max_tokens = 1500
            )
        return response.choices[0].message.content

    except Exception as e :
        return f"Error while generating explanation: {str(e)}"