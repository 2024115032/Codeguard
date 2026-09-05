from services.pr_analyzer import analyze_pull_request


owner = "2024115032"
repo = "CodeGuard-Test"
pull_number = 1

results = analyze_pull_request(owner, repo, pull_number)

print()
print("================================")
print("   CODEGUARD PR ANALYSIS")
print("================================")

for result in results:

    print()
    print("File:", result["file"])

    security = result["analysis"]["security"]
    review = result["analysis"]["code_review"]

    print()
    print("Security Issues:")

    for issue in security:
        print(f"[WARNING] {issue['type']}")
        print(f"Line: {issue['line']}")

    print()
    print("Code Quality Issues:")

    for issue in review:
        print(f"[WARNING] {issue['type']}")
        print(f"Line: {issue['line']}")

print()
print("================================")