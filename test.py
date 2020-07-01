# get the file:
import re
import sys
import pandas

regexDate = r"\[(\d*\/\d+\/\d+)\, (\d+\:\d+:\d+)\]"

regexUserName = r"\]\s([a-zA-z0-9 ]*)"
regexUserNumber = r"\+[\s+\d\s]*"
number2 = r"\+[+\s\w:]+"


def get_date_time(line):
    matchesDate = re.search(regexDate, line, re.MULTILINE)
    if matchesDate is None:
        pass
    else:
        Date = matchesDate.groups()[0]
        Time = matchesDate.groups()[1]
        return str(Date), str(Time)


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
                totalTable.append([' ', ' ', ' ', line.replace('\n', '')])
            else:
                try:
                    date, time = get_date_time(line)
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

                totalTable.append([date, time, user, message.replace('\n', '')])

    return totalTable


if __name__ == '__main__':
    try:
        fileName = str(sys.argv[1])
    except Exception:
        print("Please put a file in it")
        sys.exit()

    data = get_data(fileName)
    for i in data:
        print(i)
