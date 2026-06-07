from src.core.explainer import explain_code

def main() :
    print("Java code explainer")

    while True :
        lines = []
        print("Enter code (END to stop, quit to exit):")

        while True :
            line = input()
            if line.lower() == "quit" :
                return
            if line.lower() == "end" :
                break
            lines.append(line)
        
        code = "\n".join(lines)
        print("\nGenerating explanation...\n")
        result = explain_code(code)
        print(result)

if __name__ == "__main__":
    main()