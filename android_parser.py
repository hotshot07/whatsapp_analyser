# android parser
# android .txt files don't have seconds in timestamp
# the way it's writen is similar yet a bit different
# it doesn't use '[' for timestamp, infact it doesn't use anything at all

import re
import numpy as np
from datetime import datetime
import calendar
from dateutil import parser
import pandas as pd

regexDate = r"(\d\d\/\d\d/\d\d\d\d\, \d\d:\d\d)"
regexUserName = r"\-\s([a-zA-z0-9 ]*)"
regexUserNumber = r"\-[\s+\d\s]*:"


# Gets the date and time, changes it to iso-format
# I hope it's same across all the countries
def get_date_time_day(line):
    matchesDate = re.search(regexDate, line, re.MULTILINE)

    if matchesDate is None:
        Date, Day, Time = np.NaN, np.NaN, np.NaN

    else:
        date_and_time = matchesDate.groups()
        my_date_str = str(date_and_time[0])
        try:
            datetime_obj = parser.parse(my_date_str, dayfirst=True)
            Date = datetime_obj.date().isoformat()
            Time = datetime_obj.strftime("%H:%M:%S")
            Day = calendar.day_name[datetime_obj.weekday()]
        except:
            Date, Time, Day = np.NaN, np.NaN, np.NaN

    return Date, Day, Time


# putting regex to work here
def get_user(line):
    matchesName = re.search(regexUserName, line, re.MULTILINE)

    matchesNumber = re.search(regexUserNumber, line, re.MULTILINE)

    if matchesName is not None:
        Name = matchesName.groups()[0]
    if matchesNumber is not None:
        Number = matchesNumber.group()

    # for andorid the "this chat is secured .. message is removed"
    if Name:
        if "secured" in str(Name) or "changed" in str(Name):
            return " "
        else:
            return str(Name)
    else:
        return str(Number[1:-1])

# hack to get user messages
def get_message(line):
    colon = ':'
    counter = 0
    message = ""
    for i in range(len(line)):
        if line[i] == colon:
            counter = counter + 1

        if counter == 2:
            message = line[i + 2:]
            break

    counter = 0
    return message

# each line in txt file is parsed line by line till a newline
# character appears
def get_data(fileName):

    totalTable = []

    with open(fileName, 'r') as chat:
        for line in chat:
            # removing weird typesetting character found in front of images
            line = line.replace('\u200e', '')

            date, day, time = get_date_time_day(line)
            if date is np.NaN:
                totalTable.append([np.NaN, np.NaN, np.NaN, np.NaN, line.replace('\n', '')])
            else:
                user = get_user(line)
                message = get_message(line)
                totalTable.append([date, day, time, user, message.replace('\n', '')])

    return totalTable


# the exported function
# takes in filename as the argument
# rest are all helper functions
def android_data(fileName):
    data = get_data(fileName)

    df = pd.DataFrame(columns=['Date', 'Day', 'Time', 'User', 'Message'])

    for num, info in enumerate(data):
        df.loc[num] = info

    df.to_csv(r'userdata/chat.csv')
