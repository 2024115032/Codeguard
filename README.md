# CodeGuard – Pull Request Security & Bug Screener

## About the Project

CodeGuard is a Python-based tool that checks GitHub Pull Requests for common security and code quality issues.

When a Pull Request is created or updated, CodeGuard gets the changed files, analyzes the Python code, and posts the result as a comment in the Pull Request.

The main purpose of this project is to help developers find simple problems before merging their code.

---

## Problem

During code review, developers may miss simple issues such as:

* Hardcoded passwords
* API keys
* Secrets
* Debug print statements
* TODO comments
* Long lines
* Dangerous functions such as `eval()`

Checking these issues manually for every Pull Request takes time.

CodeGuard automates these checks and gives the result directly in GitHub.

---

## Objectives

* Check code automatically when a Pull Request is created.
* Find common security-related issues.
* Find basic code quality issues.
* Get changed files directly from GitHub.
* Generate a simple review report.
* Post the report as a comment in the Pull Request.

---

## Features

### Security Scanner

The security scanner checks for:

* Hardcoded passwords
* API keys
* Secrets
* AWS access keys

### Code Reviewer

The code reviewer checks for:

* `print()` statements
* `TODO` comments
* Lines longer than 100 characters
* `eval()` usage

### GitHub Integration

CodeGuard uses the GitHub REST API to:

1. Get the files changed in a Pull Request.
2. Analyze the changed Python files.
3. Post the analysis result as a Pull Request comment.

### Webhook

A GitHub webhook sends Pull Request events to the Flask application.

CodeGuard currently handles:

* `opened`
* `synchronize`

---

## How It Works

```text
Developer
    |
    v
Creates Pull Request
    |
    v
GitHub Webhook
    |
    v
Flask Application
    |
    v
Get Changed Files
    |
    +----------------------+
    |                      |
    v                      v
Security Scanner      Code Reviewer
    |                      |
    +----------+-----------+
               |
               v
        Generate Report
               |
               v
       GitHub PR Comment
```

---

## Project Structure

```text
Codeguard/
│
├── agents/
│   ├── __init__.py
│   ├── security_scanner.py
│   └── code_reviewer.py
│
├── services/
│   ├── __init__.py
│   ├── analyzer.py
│   ├── github_service.py
│   ├── pr_analyzer.py
│   ├── report_generator.py
│   └── review_service.py
│
├── tests/
│   ├── __init__.py
│   ├── test_security.py
│   ├── test_reviewer.py
│   ├── test_analyzer.py
│   ├── test_pr.py
│   ├── test_pr_analyzer.py
│   ├── test_report.py
│   └── test_full_review.py
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Technologies Used

* Python
* Flask
* GitHub REST API
* GitHub Webhooks
* Requests
* Python-dotenv
* Regular Expressions

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/2024115032/Codeguard.git
```

### 2. Go to the project folder

```bash
cd Codeguard
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install the required packages

```bash
pip install -r requirements.txt
```

---

## Environment Setup

Create a `.env` file in the project folder.

Add:

```text
GITHUB_TOKEN=your_github_token
```

The token is used to access the GitHub API.

The `.env` file should not be uploaded to GitHub.

---

## Run the Project

Start the Flask application:

```bash
python app.py
```

The application runs at:

```text
http://127.0.0.1:5000
```

Open the address in a browser.

You should see:

```text
CodeGuard API is running!
```

---

## API Endpoints

### Home

```text
GET /
```

Used to check whether the Flask application is running.

### Analyze Code

```text
POST /analyze
```

Analyzes the code and returns the security and code review results.

### GitHub Webhook

```text
POST /webhook
```

Receives Pull Request events from GitHub.

---

## Testing

The project contains test files for different parts of CodeGuard.

### Security Scanner

```bash
python tests/test_security.py
```

### Code Reviewer

```bash
python tests/test_reviewer.py
```

### Analyzer

```bash
python tests/test_analyzer.py
```

### GitHub PR

```bash
python tests/test_pr.py
```

### PR Analyzer

```bash
python tests/test_pr_analyzer.py
```

### Report Generator

```bash
python tests/test_report.py
```

### Full Review

```bash
python tests/test_full_review.py
```

---

## Example

For testing, the following code can be used:

```python
password = "fake_password_123"
api_key = "FAKE_API_KEY_123"

print("Debug test")

result = eval("2 + 2")
```

CodeGuard detects:

```text
Hardcoded Password
API Key
Debug Print
Dangerous Function
```

The GitHub Pull Request comment will show:

```text
## 🤖 CodeGuard Review

### 📁 app.py

#### 🔐 Security Issues

- Hardcoded Password
- API Key

#### 🧹 Code Quality Issues

- Debug Print
- Dangerous Function

Total Issues Found: 4

### ❌ Changes Required
```

---

## GitHub Integration

CodeGuard gets the changed files from a Pull Request using the GitHub REST API.

The API used is:

```text
GET /repos/{owner}/{repo}/pulls/{pull_number}/files
```

After analyzing the files, CodeGuard creates a report and posts it to the Pull Request.

This makes it possible to see the CodeGuard result directly in GitHub.

---

## Webhook Flow

The GitHub repository is connected to the Flask application using a Pull Request webhook.

The flow is:

```text
GitHub Pull Request
        |
        v
GitHub Webhook
        |
        v
Flask /webhook
        |
        v
Analyze Pull Request
        |
        v
Generate Report
        |
        v
Post Comment to GitHub
```

---

## Result

CodeGuard was tested using a GitHub Pull Request containing sample security and code quality issues.

The system successfully detected:

```text
Hardcoded Password
API Key
Debug Print
Dangerous Function
```

and posted the result automatically as a comment in the Pull Request.

---

## Limitations

The current version mainly checks Python files.

The implemented checks use predefined rules and patterns. It does not currently use an external LLM API.

---

## Future Improvements

Some possible improvements are:

* Add LLM-based code analysis.
* Add more security checks.
* Support other programming languages.
* Add dependency vulnerability checking.
* Give suggestions for fixing detected issues.
* Add automated test execution.

---

## Project Information

**Project:** CodeGuard – Pull Request Security & Bug Screener

**Language:** Python

**Framework:** Flask

**Platform:** GitHub

**GitHub Integration:** GitHub REST API and GitHub Webhooks
