# CAUTION: before running the code, see README.md
# not sure what to fill in? refer to the REAME.md on how to use this bot

from code import Bot

# initialize bot
sba_bot = Bot()

# login
sba_bot.login(username="", password="")

# Entering English Marks
sba_bot.select_subject(name="ENGLISH LANGUAGE", status_code="L").enter_data(file="data\data.csv")

# Entering English Marks
sba_bot.select_subject(name="INTEGRATED SCIENCE", status_code="L").enter_data(file="data\data.csv")
