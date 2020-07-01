# get the file:

import re

regexDate = r"\[(\d*\/\d+\/\d+)\, (\d+\:\d+:\d+)\]"

regexUserName = r"\]\s([a-zA-z0-9 ]*)"
regexUserNumber = r"\+[\s+\d\s]*"
number2 = r"\+[+\s\w:]+"


with open('chat2.txt', 'r') as chat:

    for line in chat:
        matchesDate = re.search(regexDate, line, re.MULTILINE)
        if matchesDate is None:
            pass
        else:
            Date = matchesDate.groups()[0]
            Time = matchesDate.groups()[1]
            print(Date, Time)

        matchesName = re.search(regexUserName, line, re.MULTILINE)

        matchesNumber = re.search(regexUserNumber, line, re.MULTILINE)

        if matchesName is not None:
            print(matchesName.groups()[0])
        if matchesNumber is not None:
            print(matchesNumber.group())

        colon = ':'
        counter = 0
        for i in range(len(line)):
            if line[i] == colon:
                counter = counter + 1

            if counter == 3:
                print(line[i + 2:])
                break

        counter = 0
