def generate_report(results):

    report = []

    report.append("## 🤖 CodeGuard Review")
    report.append("")

    total_issues = 0

    for result in results:

        filename = result["file"]

        report.append(f"### 📁 {filename}")
        report.append("")

        security = result["analysis"]["security"]
        review = result["analysis"]["code_review"]

        if security:
            report.append("#### 🔐 Security Issues")

            for issue in security:
                report.append(
                    f"- ⚠️ **{issue['type']}** — Line {issue['line']}"
                )

            report.append("")

        if review:
            report.append("#### 🧹 Code Quality Issues")

            for issue in review:
                report.append(
                    f"- ⚠️ **{issue['type']}** — Line {issue['line']}"
                )

            report.append("")

        total_issues += len(security) + len(review)

    report.append("---")
    report.append(f"**Total Issues Found: {total_issues}**")
    report.append("")

    if total_issues > 0:
        report.append("### ❌ Changes Required")
    else:
        report.append("### ✅ Approved")

    return "\n".join(report)