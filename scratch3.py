from config import setup_lm
from pipeline import Helpdesk

setup_lm()
bot = Helpdesk()
out = bot(ticket="I was charged twice for my annual plan. Please fix this today!")
print(out.category, out.urgency)
print(out.reply)