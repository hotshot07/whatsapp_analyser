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
        return Date, Time


def get_user(line):
    matchesName = re.search(regexUserName, line, re.MULTILINE)

    matchesNumber = re.search(regexUserNumber, line, re.MULTILINE)

    if matchesName is not None:
        Name = matchesName.groups()[0]
    if matchesNumber is not None:
        Number = matchesNumber.group()

    if Name:
        return Name
    else:
        return Number


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

    if fileName is None:

        sys.exit()

    with open(fileName, 'r') as chat:
        for line in chat:
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

            print(date, time, user, message)


if __name__ == '__main__':
    fileName = str(sys.argv[1])
    if fileName is None:
        print("Please put a file init na madarchod")
        sys.exit()
    else:
        get_data(fileName)
