from services.pr_analyzer import analyze_pull_request
from services.report_generator import generate_report
from services.github_service import post_pull_request_comment


def review_pull_request(owner, repo, pull_number):

    results = analyze_pull_request(
        owner,
        repo,
        pull_number
    )

    report = generate_report(results)

    post_pull_request_comment(
        owner,
        repo,
        pull_number,
        report
    )

    return report