from services.github_service import post_pull_request_comment


owner = "2024115032"
repo = "CodeGuard-Test"
pull_number = 1

comment = """🤖 CodeGuard Test

CodeGuard successfully connected to this Pull Request.
"""

result = post_pull_request_comment(
    owner,
    repo,
    pull_number,
    comment
)

print("GitHub comment posted successfully!")
print("Comment ID:", result["id"])