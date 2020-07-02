import re
import sys
import numpy as np
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
from datetime import datetime
import calendar
from dateutil import parser

#pd.options.display.width = 0

regexDate = r"\[(\d*\/\d+\/\d+)\, (\d+\:\d+:\d+)\]"
regexUserName = r"\]\s([a-zA-z0-9 ]*)"
regexUserNumber = r"\+[\s+\d\s]*"
number2 = r"\+[+\s\w:]+"


def get_date_time_day(line):
    matchesDate = re.search(regexDate, line, re.MULTILINE)

    if matchesDate is None:
        Date, Day, Time = np.NaN, np.NaN, np.NaN

    else:
        Date = matchesDate.groups()[0]
        Time = matchesDate.groups()[1]
        my_date_str = str(Date) + ' ' + str(Time)
        try:
            datetime_obj = parser.parse(my_date_str)
            Date = datetime_obj.date().isoformat()
            Time = datetime_obj.strftime("%H:%M:%S")
            Day = calendar.day_name[datetime_obj.weekday()]
        except:
            Date, Time, Day = np.NaN, np.NaN, np.NaN

    print(Date, Day, Time)
    return Date, Day, Time


def get_user(line):
    matchesName = re.search(regexUserName, line, re.MULTILINE)

    matchesNumber = re.search(regexUserNumber, line, re.MULTILINE)

    if matchesName is not None:
        Name = matchesName.groups()[0]
    if matchesNumber is not None:
        Number = matchesNumber.group()

    if Name:
        return str(Name)
    else:
        return str(Number)


def get_message(line):
    colon = ':'
    counter = 0
    for i in range(len(line)):
        if line[i] == colon:
            counter = counter + 1

        if counter == 3:
            message = line[i + 2:]
            break

    counter = 0
    return message


def get_data(fileName):

    totalTable = []
    with open(fileName, 'r') as chat:
        for line in chat:
            line = line.replace('\u200e', '')
            if line[0] != '[':
                totalTable.append([' ', ' ', ' ', ' ', line.replace('\n', '')])
            else:
                try:
                    date, day, time = get_date_time_day(line)
                except:
                    pass

                try:
                    user = get_user(line)
                except:
                    pass

                try:
                    message = get_message(line)
                except:
                    pass

                totalTable.append([date, day, time, user, message.replace('\n', '')])

    return totalTable


if __name__ == '__main__':
    try:
        fileName = str(sys.argv[1])
        if not fileName.endswith('.txt'):
            print("Please put a whatsapp .txt file")
            sys.exit()
    except Exception:
        print("Please put a file in it")
        sys.exit()

    data = get_data(fileName)

    df = pd.DataFrame(columns=['Date', 'Day', 'Time', 'User', 'Message'])

    for num, info in enumerate(data):
        df.loc[num] = info

    df.to_csv(r'userdata/chat.csv')
