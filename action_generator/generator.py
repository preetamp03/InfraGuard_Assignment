import json

def generate_action_summary(issue, decision_type):
    """
    Turn a decision into a simulated PR/ticket format
    """
    title = issue.get("issue", "Security Issue")

    if decision_type == "Act":
        heading = "### ✅ Immediate Action Required\nThis issue requires an automated fix or PR."
    elif decision_type == "Escalate":
        heading = "### ⚠️ Escalation Required\nThis issue should be reviewed by a human engineer."
    else:
        heading = "### 💡 Suggestion\nThis is a best-practice tip for improvement."

    body = (
        f"## 🛡️ Issue: {title}\n\n"
        f"{heading}\n\n"
        f"#### 🔍 Details:\n```json\n{json.dumps(issue, indent=2)}\n```"
    )

    return {
        "title": f"{decision_type}: {title}",
        "body": body,
        "action_type": decision_type
    }
