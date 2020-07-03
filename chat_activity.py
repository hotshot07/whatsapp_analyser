import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
import datetime
import random
from datetime import date

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

for x in manage_labels:
    if type(x) is datetime.date and random.random() < 0.3:
        final_labels.append(x.strftime("%B %d, %Y"))
    else:
        final_labels.append('')


plt.figure(figsize=(25, 10))


chart = sns.barplot(final_data["Date"], final_data["Messages"], alpha=1, palette='rocket', data=final_data)

chart.set_xticklabels(final_labels, rotation=90, fontweight='light', horizontalalignment='center', fontsize=6)
plt.tight_layout()
plt.show()
