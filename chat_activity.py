import datetime
from datetime import date
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


def timeline(p_num):
    df = pd.read_csv("userdata/chat.csv")

    df_day = dict(df["Date"].dropna().value_counts(sort=False))

    date_range = pd.date_range(start=str(df["Date"][0]), end=str(df["Date"][df.index[-1]]))

    chat_list = []

    manage_labels = []

    for i in date_range:
        if str(i.date()) in df_day.keys():
            chat_list.append(df_day[str(i.date())])
            manage_labels.append((i.date()))
        else:
            chat_list.append(0)
            manage_labels.append("")

    final_data = date_range.to_frame(name="Date", index=False)

    final_data["Messages"] = chat_list

    final_labels = []

    def get_spacing():
        total_len = len(chat_list)
        SPACING = 2
        for i in range(0, total_len, 365):
            SPACING += 1

        return SPACING

    SPACING = get_spacing()

    for num, x in enumerate(manage_labels):
        if type(x) is datetime.date and num % SPACING == 0 or num == 0 or num == len(manage_labels) - 1:
            final_labels.append(x.strftime("%B %d, %Y"))
        else:
            final_labels.append('')

    plt.figure(p_num, figsize=(20, 10))
    sns.set_context("paper")
    chart = sns.barplot(final_data["Date"], final_data["Messages"], alpha=1, palette='husl', data=final_data)
    #chart.set(xlabel='Timeline', ylabel='Messages')
    # plt.figure(num=p_num)
    plt.xlabel('Timeline', fontsize=18, fontname="Andale Mono")
    plt.ylabel('Messages exchanged', fontsize=16, fontname="Andale Mono")
    plt.title('Chat Activity', fontsize=20, fontname="Andale Mono")
    chart.set_xticklabels(final_labels, rotation=90, fontweight='light', horizontalalignment='center', fontsize=6)
    plt.tight_layout()
    plt.savefig("output/timeline.png")
    return 1
