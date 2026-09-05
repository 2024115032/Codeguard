from agents.security_scanner import scan_security
from agents.code_reviewer import review_code


def analyze_code(code):
    security_issues = scan_security(code)
    review_issues = review_code(code)

    return {
        "security": security_issues,
        "code_review": review_issues
    }