import dspy


def _ex(ticket, category, urgency):
    return dspy.Example(ticket=ticket, category=category, urgency=urgency).with_inputs("ticket")


trainset = [
    _ex("I was charged twice for my annual plan this month. Please fix this today, it's a lot of money.", "billing", "high"),
    _ex("The desktop app stopped syncing my notes since yesterday and I have a presentation in an hour!", "technical", "high"),
    _ex("How do I change the email address on my account?", "account", "low"),
    _ex("It would be great if you added a dark mode to the mobile app.", "feature_request", "low"),
    _ex("I can't log in. It says my password is wrong but I just reset it.", "account", "medium"),
    _ex("Can I get a refund? I bought the annual plan two weeks ago and no longer need it.", "billing", "medium"),
    _ex("The web editor crashes whenever I paste an image larger than 5 MB.", "technical", "medium"),
    _ex("Do you have a student discount?", "billing", "low"),
    _ex("Our whole team lost access to the shared workspace and we are blocked from working.", "technical", "high"),
    _ex("Please add the ability to export notes as Markdown files.", "feature_request", "low"),
]

devset = [
    _ex("I see two identical charges on my credit card statement for the same day.", "billing", "high"),
    _ex("How can I turn on two-factor authentication?", "account", "low"),
    _ex("Notes I created on my phone are not showing up on my laptop.", "technical", "medium"),
    _ex("Could you support tags with colors? I organise everything visually.", "feature_request", "low"),
    _ex("I want to delete my account and all my data.", "account", "medium"),
    _ex("Your app is awesome, just wanted to say thanks to the team!", "other", "low"),
    _ex("My invoice shows the wrong company name and I need a corrected one for tax filing next week.", "billing", "medium"),
    _ex("The app shows a blank white screen on startup since the last update and I can't access anything.", "technical", "high"),
    _ex("Where can I find your office address?", "other", "low"),
    _ex("How do I downgrade from Pro to Basic at the end of this billing cycle?", "billing", "low"),
]