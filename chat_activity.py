import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
import datetime

from datetime import date

df = pd.read_csv("userdata/chat.csv")

df_day = dict(df["Date"].dropna().value_counts(sort=False))

# print(df_day)

date_range = pd.date_range(start=str(df["Date"][0]), end=str(df["Date"][df.index[-1]]))

chat_list = []

for i in date_range:
    if str(i.date()) in df_day.keys():
        chat_list.append(df_day[str(i.date())])
    else:
        chat_list.append(0)

final_data = date_range.to_frame(name="Date", index=False)

final_data["Messages"] = chat_list

plt.figure(figsize=(20, 10))

#chart = sns.lineplot(final_data["Date"], final_data["Messages"])

#chart.set_xticklabels(chart.get_xticklabels(), rotation=90)

# df['week_number_of_year'] = datetime.date(df['Date'][0]).dt.week

# week_number_of_year = []

# for i in range(len(df["Date"])):
#     try:
#         date_obj = datetime.date.fromisoformat(df['Date'][i])
#         string_obj = str(date_obj.isocalendar()[0]) + '_' + str(date_obj.isocalendar()[1])
#         week_number_of_year.append(string_obj)
#     except:
#         week_number_of_year.append(" ")


# df["Year_week"] = week_number_of_year

# df_day2 = df["Year_week"].value_counts()

# df_day = sorted(dict(df_day2))
# df_day.remove(' ')

# df_day3 = {}
# for i in df_day:
#     df_day3[str(i)] = df_day2[i]

# print(df_day3)
sns.scatterplot(final_data["Date"], final_data["Messages"], alpha=0.8, palette='rocket', data=final_data)

plt.show()

# date_obj = datetime.datetime.strptime(df['Date'][i], '%Y-%m-%d')
#         print(date_obj)
#         print(date_obj.date().isoformat().isocalendar())
#         print()
