from src.core.explainer import explain_code
from rich.console import Console # main output manager, supports colors, borders etc
from rich.panel import Panel # boxes around text
from rich.syntax import Syntax # syntax highlighting for code

import time 

console = Console()

def main() :

    console.print("[bold cyan]Code Explainer[/bold cyan]")

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
        
        console.print("\n[yellow]Generating explanation[/yellow]\n")

        syntax = Syntax(
            code,
            language,
            theme="monokai",
            line_numbers=True
        )

        console.print(
            Panel(
                syntax,
                title="Input Code"
            )
        )

        with console.status(
            "[bold green]Analyzing code..."
        ): result = explain_code(language,code)  # for adding loading spinner

        console.print(
            Panel(
            result,
            title="Explanation",
            border_style="green"
            )
)

if __name__ == "__main__":
    main()