import re


def scan_security(code):
    issues = []

    patterns = {
        "Hardcoded Password": r'password\s*=\s*["\'].*["\']',
        "API Key": r'(api_key|apikey)\s*=\s*["\'].*["\']',
        "Secret": r'secret\s*=\s*["\'].*["\']',
        "AWS Access Key": r'AKIA[0-9A-Z]{16}',
    }

    lines = code.splitlines()

    for line_number, line in enumerate(lines, start=1):

        for issue_name, pattern in patterns.items():

            if re.search(pattern, line, re.IGNORECASE):

                issues.append({
                    "type": issue_name,
                    "line": line_number,
                    "code": line.strip()
                })

    return issues