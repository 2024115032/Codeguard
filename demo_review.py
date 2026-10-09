
from services.analyzer import analyze_code
from services.report_generator import generate_report

# TEST 1: Code with security and quality issues
unsafe_code = '''
password = "admin123"
api_key = "ABC123XYZ"
print("Debug test")
result = eval("2 + 2")
'''

# TEST 2: Clean sample code
clean_code = '''
def add_numbers(a, b):
    return a + b
'''

def run_demo(title, code):
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)

    analysis = analyze_code(code)

    results = [
        {
            "file": "sample_app.py",
            "analysis": analysis
        }
    ]

    print(generate_report(results))


run_demo("TEST 1: CODE WITH ISSUES", unsafe_code)
run_demo("TEST 2: CLEAN CODE", clean_code)