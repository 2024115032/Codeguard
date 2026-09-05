from services.github_service import get_pull_request_files
from services.analyzer import analyze_code


def analyze_pull_request(owner, repo, pull_number):

    files = get_pull_request_files(owner, repo, pull_number)

    results = []

    for file in files:

        filename = file["filename"]

        if not filename.endswith(".py"):
            continue

        patch = file.get("patch", "")

        analysis = analyze_code(patch)

        results.append({
            "file": filename,
            "analysis": analysis
        })

    return results