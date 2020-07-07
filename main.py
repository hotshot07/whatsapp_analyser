import sys
import os
from ios_parser import ios_data
from android_parser import android_data
from wc import make_wordcloud
from weekday_vis import make_week_vis
from user_activity import user_activity_vis
from chat_activity import timeline


if __name__ == '__main__':
    fileName = ''
    os_type = ''

    # Parsing the user input
    try:
        os_type = str(sys.argv[1].lower())
        if os_type not in "ios android":
            print("Please put a valid os name")
            sys.exit()
    except Exception:
        print("Please put an os name")
        sys.exit()

    try:
        fileName = str(sys.argv[2])
        if not fileName.endswith('.txt'):
            print("Please put a whatsapp .txt file")
            sys.exit()
    except Exception:
        print("Please put the file path correctly")
        sys.exit()

    # Creating Directory
    if not os.path.exists('output'):
        os.makedirs('output')

    if not os.path.exists('userdata'):
        os.makedirs('userdata')

    # Parsing the .txt file
    # ios and android users have different styles of storing data
    # it produces output in userdata/chat.csv
    print("Processing data ...")
    if sys.argv[1] == 'ios':
        ios_data(fileName)
    else:
        android_data(fileName)

    # numbers have been passed to avoid conflicts with multiple
    # plt figures
    # lets not be afraid to ask for help
    # https://stackoverflow.com/questions/62737270/matplotlib-import-issue-across-modules

    print("Creating word cloud ...")
    make_wordcloud(1)

    print("Creating weekday visualization ...")
    make_week_vis(2)

    print("Creating timeline ...")
    timeline(3)

    print("Creating user activity ...")
    user_activity_vis(4)

    print("Done! Please check the output folder")
