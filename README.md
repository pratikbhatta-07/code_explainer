# 🚀 Code Explainer

Code Explainer is a **command-line AI-powered developer tool** that analyzes source code and provides structured insights using Large Language Models (LLMs).

It goes beyond simple explanations by combining **tool orchestration, caching, and modular system design** to simulate a real-world AI engineering pipeline.

---

## 🔥 Key Features

### 🧠 Multi-Language Code Analysis
Supports multiple languages:
- Python
- Java
- C++
- JavaScript
- Extensible to others

---

### ⚙️ Multiple Analysis Modes

- **Beginner Friendly Explanation**  
  → Step-by-step explanation with analogies  

- **Interview Style Analysis**  
  → Optimized for DSA + interview prep  

- **Unit Test Generation**  
  → Generates framework-specific test cases  

- **Full Review Pipeline**  
  → Combines explanation + complexity + testing  

---

### ⚡ SQLite-Based Smart Caching (NEW)

- Persistent caching using **SQLite (instead of JSON)**
- Avoids redundant LLM API calls
- Hash-based cache keys for fast lookup
- Improves performance and reduces API usage

---

### 🧩 Modular Tool Architecture

- Explanation Tool
- Complexity Tool
- Test Generation Tool

Each tool is independent and reusable.

---

### 🧠 Intelligent Orchestration

- Central orchestrator manages:
  - Tool execution
  - Response aggregation
  - Pipeline flow

---

### 📂 Flexible Input System

- Paste code directly
- Provide file input

---

### 📊 Complexity Analysis

- Estimates:
  - Time Complexity
  - Space Complexity
- Uses lightweight static analysis

---

### 🧪 Automated Unit Test Generation

- Python → pytest/unittest  
- Java → JUnit  
- JavaScript → Jest  
- C++ → Google Test  

---

### 💻 Rich CLI Experience

- Syntax highlighting  
- Structured panels  
- Clean output  
- Interactive prompts  

---

## 🏗️ Architecture

```text
User Input
    │
    ▼
CLI Layer
    │
    ▼
Orchestrator
    │
    ├── Explanation Tool  (LLM + Cache)
    ├── Complexity Tool   (Static Analysis)
    ├── Test Tool         (LLM + Cache)
    │
    ▼
Service Layer
    │
    ├── Groq API Service
    └── Cache Service (SQLite)
    │
    ▼
SQLite Database
    │
    ▼
Formatted Output (CLI)

## 📁 Project Structure

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
│   └── cache_services.py
│
├── db/
│   ├── db.py
│   └── init_db.py
│
├── utils/
│   └── config.py
│
data/
│   └── cache.db
│
requirements.txt
README.md


## ⚙️ Installation

git clone https://github.com/pratikbhatta-07/code_explainer.git
cd code_explainer
pip install -r requirements.txt


## ▶️ Running the Application

python3 -m src.cli.main

## Author -
PRATIK BHATTA