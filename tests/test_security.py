from agents.security_scanner import scan_security


code = '''
password = "admin123"
api_key = "ABC123XYZ"
name = "Abinaya"
'''

results = scan_security(code)

print("CODEGUARD SECURITY SCAN")
print("=======================")

for issue in results:
    print(f"[WARNING] {issue['type']}")
    print(f"Line: {issue['line']}")
    print(f"Code: {issue['code']}")
    print()