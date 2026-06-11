from src.core.orchestrator import full_review
from src.tools.explanation_tool import explain_code
from src.db.init_db import init_db

from rich.console import Console # main output manager, supports colors, borders etc
from rich.panel import Panel # boxes around text
from rich.syntax import Syntax # syntax highlighting for code

console = Console()

def main() :

    console.print("[bold cyan]Code Explainer[/bold cyan]")

    while True :

        #LANGUAGE INPUT
        language = input("Enter language (java, c, c++, python, js) or type quit to exit : ").strip()
        if language.lower() == "quit" or language.lower() == "exit" :
            return
        
        #MODE INPUT
        mode = input("Enter mode\n 1. Beginner friendly\n 2. Interview style\n 3. Unit Test Generation\n 4. Full Review\n Choose mode : ").strip().lower()
        
        #CHOICE INPUT
        choice = input("Enter input style\n 1. Paste code\n 2. File Input\n Choose : ")

        if choice == "1" :
            if language.lower() == "quit" :
                return
            lines = []
            print("Enter code or end to stop or quit to exit):")

            while True :
                line = input()
                
                if line.lower() == "end" :
                    break
                lines.append(line)
        
            code = "\n".join(lines)
        
        elif choice == "2" :
            path = input("Enter input file path : ")
            if path.lower() in ["quit", "exit"]:
                return
            
            try :
                with open(path, "r") as f :
                    code = f.read()
            except FileNotFoundError :
                console.print("[red]Invalid File Path[/red]")
                continue
        
        else :
            console.print("[red]Invalid Input[/red]")
            continue
        
        console.print("\n[yellow]Generating explanation[/yellow]\n")

        syntax = Syntax(
            code,
            language,
            theme="monokai",
            line_numbers=True
        )

        #CODE FOR PRINTING INPUT CODE IN THE OUTPUT SCREEN
        console.print(
            Panel(
                syntax,
                title="Input Code"
            )
        )
        
        #LOADING WHEEL AND DEFINING RESULT
        with console.status(
            "[bold green]Analyzing code..."
        ): 
            if mode == "4" :
                result = full_review(code, language)
            else : 
                result = explain_code(code, language, mode)  # for adding loading spinner

        console.print(
            Panel(
            result,
            title="Explanation",
            border_style="green"
            )
)

if __name__ == "__main__":
    init_db()
    main()