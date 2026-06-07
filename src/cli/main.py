from src.core.explainer import explain_code

def main() :

    print("Code Explainer")

    while True :

        language = input("Enter language (java, c, c++, python, js) or type quit to exit : ").strip()
        if language.lower() == "quit" :
            return
        lines = []
        print("Enter code or end to stop or quit to exit):")

        while True :
            line = input()
            if line.lower() == "quit" or line.lower() == "exit" or line.lower() == "no" :
                return
            if line.lower() == "end" :
                break
            lines.append(line)
        
        code = "\n".join(lines)
        print("\nGenerating explanation...\n")
        result = explain_code(language,code)
        print(result)

if __name__ == "__main__":
    main()