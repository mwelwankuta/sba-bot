# G7 Ecz School Based Assesment Bot

entering learners exam marks takes a long time, this project makes it easier to submit SBA results for learner withing a short period of time

<hr/>

## Entering Marks Duration
- #### With the SBA Bot `5 minutes`
- #### Without the SBA Bot `2 hours`


to use the SBA bot, your csv data needs to be arranged by exam number
your csv file's information should be arranged exactly like the example below.

|SN| EXAM | NAME | MATH | ENG | SCIE | BEMBA | CTS | SS|
|---|--------|-----------|------|-----|------|-------|-----|---|
| 1 | 145264 | Learner | 30 | 30 | 30 | 30 | 30 | 30|

## The Following are examples of how information should be passed

```js
--- status code---:  
( L / X / -)
```

```js
--- subject name ---: 
ENGLISH LANGUAGE, SOCIAL STUDIES, CREATIVE AND TECHNOLOGY STUDIES
ICIBEMBA, INTEGRATED SCIENCE 
```

## Initializing a bot

```py
# import bot class
from code import Bot

# bot init
sba_bot = Bot()

# login
sba_bot.login(username="user/2021", password="strong_password")

# select subject & enter data
sba_bot.subject_name(name="ENGLISH LANGUAGE", status_code="L").set_data(file="data\data.csv")

```

## File Structure

| Folder | Description                 |
| ------ | --------------------------- |
| data   | contains `csv` file of data |

## What i learnt
headless browsing with `selenium` and `python`

might not work for other gra
