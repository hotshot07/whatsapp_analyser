from ios_parser import ios_data
from android_parser import android_data
from wc import make_wordcloud
from weekday_vis import make_week_vis
from user_activity import user_activity_vis
from chat_activity import timeline
import sys


if __name__ == '__main__':
    fileName = ''
    os_type = ''
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
        print("Please put a file in it")
        sys.exit()

    print("Processing data ...")
    if sys.argv[1] == 'ios':
        ios_data(fileName)
    else:
        android_data(fileName)

    print("Creating WordCloud ...")
    make_wordcloud(1)

    print("Creating weekday visualization ...")
    make_week_vis(2)

    print("Creating Timeline ...")
    timeline(3)

    print("Getting user activity ...")
    user_activity_vis(4)

    print("Done! Please check the output folder")
