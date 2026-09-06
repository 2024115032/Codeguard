from services.review_service import review_pull_request


owner = "2024115032"
repo = "CodeGuard-Test"
pull_number = 1


print("================================")
print("   CODEGUARD FULL PR REVIEW")
print("================================")
print()

report = review_pull_request(
    owner,
    repo,
    pull_number
)

print(report)

print()
print("================================")
print("Review completed successfully!")
print("================================")