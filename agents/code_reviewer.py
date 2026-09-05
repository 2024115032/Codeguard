def review_code(code):
    issues = []

    lines = code.splitlines()

    for line_number, line in enumerate(lines, start=1):

        if "print(" in line:
            issues.append({
                "type": "Debug Print",
                "line": line_number,
                "message": "Remove print statements before production."
            })

        if "TODO" in line:
            issues.append({
                "type": "TODO",
                "line": line_number,
                "message": "Incomplete task found."
            })

        if len(line) > 100:
            issues.append({
                "type": "Long Line",
                "line": line_number,
                "message": "Line is longer than 100 characters."
            })

        if "eval(" in line:
            issues.append({
                "type": "Dangerous Function",
                "line": line_number,
                "message": "Avoid using eval()."
            })

    return issues