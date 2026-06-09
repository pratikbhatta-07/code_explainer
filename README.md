# Code Explainer

Code Explainer is a command-line application that uses Large Language Models (LLMs) to analyze source code and provide developer-focused insights. The tool supports multiple programming languages and can explain code, generate unit tests, estimate complexity, and provide interview-oriented analysis.

The project was built to explore practical applications of Generative AI in software engineering workflows and to demonstrate prompt engineering, tool orchestration, caching, and modular system design.

## Features

* Multi-language code analysis

  * Java
  * Python
  * C++
  * JavaScript
  * Other supported languages

* Multiple analysis modes

  * Beginner Friendly Explanation
  * Interview Style Analysis
  * Unit Test Generation
  * Full Review Pipeline

* File Input Support

  * Analyze code directly from source files

* Complexity Analysis

  * Estimates time and space complexity using lightweight static analysis

* Automated Unit Test Generation

  * Generates framework-specific test cases based on the provided code

* Response Caching

  * Avoids repeated API calls for previously analyzed code
  * Improves performance and reduces API usage

* Rich CLI Interface

  * Syntax highlighting
  * Structured output panels
  * Progress indicators

## Architecture

```text
User Input
    │
    ▼
CLI Layer
    │
    ▼
Orchestrator
    │
    ├── Explanation Tool
    ├── Complexity Tool
    ├── Test Generation Tool
    │
    ▼
LLM Service
    │
    ▼
Formatted Output
```

## Project Structure

```text
src/
│
├── cli/
│   └── main.py
│
├── core/
│   └── orchestrator.py
│
├── tools/
│   ├── explanation_tool.py
│   ├── complexity_tool.py
│   └── test_tool.py
│
├── services/
│   ├── groq_services.py
│   └── cache_service.py
│
cache/
│   └── cache.json
│
requirements.txt
README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/pratikbhatta-07/code_explainer.git
cd code_explainer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

## Running the Application

```bash
python3 -m src.cli.main
```

## Example Workflow

1. Select a programming language
2. Choose an analysis mode
3. Paste code or provide a file path
4. Receive a detailed analysis report

## Technologies Used

* Python
* Groq API
* Llama 3.1
* Rich
* dotenv

## Future Improvements

* Bug Detection Tool
* Retrieval-Augmented Generation (RAG)
* Web Interface
* AST-Based Complexity Analysis
* Agentic Tool Selection
* Documentation Generation
* Multi-Agent Review Pipeline

## Learning Outcomes

This project helped explore:

* Prompt Engineering
* LLM Integration
* Tool-Oriented Architecture
* Caching Strategies
* CLI Application Development
* AI-Assisted Software Engineering
* Modular Python Design

## Author

Pratik Bhatta