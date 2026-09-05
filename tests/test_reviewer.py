from agents.code_reviewer import review_code


code = '''
print("Hello")
# TODO: fix this
result = eval("2 + 2")
'''

results = review_code(code)

print("CODEGUARD CODE REVIEW")
print("=====================")

for issue in results:
    print(f"[WARNING] {issue['type']}")
    print(f"Line: {issue['line']}")
    print(f"Message: {issue['message']}")
    print()