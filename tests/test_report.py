from services.report_generator import generate_report


results = [
    {
        "file": "test.py",
        "analysis": {
            "security": [
                {
                    "type": "Hardcoded Password",
                    "line": 2
                },
                {
                    "type": "API Key",
                    "line": 3
                }
            ],
            "code_review": [
                {
                    "type": "Debug Print",
                    "line": 5
                },
                {
                    "type": "TODO",
                    "line": 7
                }
            ]
        }
    }
]


report = generate_report(results)

print(report)