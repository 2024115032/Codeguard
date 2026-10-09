
from services.analyzer import analyze_code
from services.report_generator import generate_report

sample_code = '''
password = "admin123"
api_key = "ABC123XYZ"
print("Debug test")
result = eval("2 + 2")
'''

analysis = analyze_code(sample_code)

results = [
    {
        "file": "sample_app.py",
        "analysis": analysis
    }
]

print(generate_report(results))