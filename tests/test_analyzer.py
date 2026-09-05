from services.analyzer import analyze_code


code = '''
password = "admin_123"
api_key = "API_key_2006"

print("Hello")
# TODO: fix this
result = eval("2 + 2")
'''

result = analyze_code(code)

print()
print("================================")
print("       CODEGUARD REPORT")
print("================================")

print()
print("SECURITY ISSUES")
print("----------------")

for issue in result["security"]:
    print(f"[WARNING] {issue['type']}")
    print(f"Line: {issue['line']}")
    print(f"Code: {issue['code']}")
    print()

print("CODE QUALITY ISSUES")
print("-------------------")

for issue in result["code_review"]:
    print(f"[WARNING] {issue['type']}")
    print(f"Line: {issue['line']}")
    print(f"Message: {issue['message']}")
    print()

total = len(result["security"]) + len(result["code_review"])

print("================================")
print(f"Total Issues Found: {total}")

if total > 0:
    print("Overall Status: CHANGES REQUIRED")
else:
    print("Overall Status: APPROVED")

print("================================")