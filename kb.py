import re

KB = [
    {"title": "Refund policy",
     "text": "Annual plans can be refunded within 30 days of purchase. Monthly plans are not refundable but can be cancelled any time. Refunds take 5-10 business days to appear."},
    {"title": "Duplicate charges",
     "text": "If you were charged twice, the duplicate is automatically refunded within 5 business days. Contact support with the last four digits of your card if it is not refunded."},
    {"title": "Password reset",
     "text": "Use 'Forgot password' on the login page. The reset link expires after 30 minutes. If the link says it is invalid, request a new one and use the latest email only."},
    {"title": "Sync problems",
     "text": "If notes do not sync, sign out and back in, check that you are on the latest app version, and make sure you have storage space left. Sync can take up to 5 minutes on large notebooks."},
    {"title": "Export data",
     "text": "Notes can be exported as PDF or HTML from Settings > Export. Markdown export is not available yet but is on the roadmap."},
    {"title": "Change plan",
     "text": "Go to Settings > Billing to upgrade or downgrade. Downgrades take effect at the end of the current billing cycle. Students get 50% off with a valid .edu address."},
    {"title": "Delete account",
     "text": "Go to Settings > Account > Delete account. Deletion is permanent and removes all notes after 14 days. You can cancel deletion by logging in during that period."},
    {"title": "Two-factor authentication",
     "text": "Enable 2FA in Settings > Security > Two-factor authentication. Scan the QR code with an authenticator app and save your backup codes."},
    {"title": "Change email",
     "text": "Go to Settings > Account > Email. A confirmation link is sent to the new address and must be clicked within 24 hours."},
    {"title": "Invoices",
     "text": "Invoices are available in Settings > Billing > Invoices. To correct the company name or tax ID, reply to the invoice email and support will reissue it within 2 business days."},
    {"title": "Storage limits",
     "text": "Basic includes 5 GB and Pro includes 100 GB. Images larger than 20 MB are not supported in the editor."},
]

STOPWORDS = {"the", "a", "an", "is", "to", "i", "my", "of", "and", "in", "on", "for",
             "how", "do", "can", "it", "you", "me", "with", "that", "this", "your", "are"}


def _tokens(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]+", text.lower())) - STOPWORDS


def search_kb(query: str) -> list[str]:
    """Search the Cumulo knowledge base. Returns up to 2 relevant articles as 'Title: text'."""
    q = _tokens(query)
    scored = []
    for doc in KB:
        score = len(q & _tokens(doc["title"] + " " + doc["text"]))
        if score:
            scored.append((score, f"{doc['title']}: {doc['text']}"))
    scored.sort(reverse=True)
    return [text for _, text in scored[:2]] or ["No matching article found."]


def kb_as_text() -> str:
    """The whole KB as one string (used by the judge in the evaluation step)."""
    return "\n".join(f"{d['title']}: {d['text']}" for d in KB)