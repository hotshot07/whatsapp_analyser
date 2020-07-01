# get the file:

import re

regexDate = r"\[(\d*\/\d+\/\d+)\, (\d+\:\d+:\d+)\]"

regexUserName = r"\]\s([a-zA-z0-9 ]*)"
regexUserNumber = r""

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
        if matchesName is not None:
            print(matchesName.groups())
