from services.github_service import get_pull_request_files


owner = "2024115032"
repo = "CodeGuard-Test"
pull_number = 1

files = get_pull_request_files(owner, repo, pull_number)

print("CODEGUARD GITHUB PR TEST")
print("========================")

for file in files:
    print("File:", file["filename"])
    print("Status:", file["status"])
    print("Changes:", file["changes"])
    print()