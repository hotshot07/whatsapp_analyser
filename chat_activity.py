import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
import datetime

from datetime import date

df = pd.read_csv("userdata/chat.csv", index_col=0)

# df['week_number_of_year'] = datetime.date(df['Date'][0]).dt.week

week_number_of_year = []

for i in range(len(df["Date"])):
    try:
        date_obj = datetime.date.fromisoformat(df['Date'][i])
        string_obj = str(date_obj.isocalendar()[0]) + '_' + str(date_obj.isocalendar()[1])
        week_number_of_year.append(string_obj)
    except:
        week_number_of_year.append(" ")


df["Year_week"] = week_number_of_year

print(df)

# date_obj = datetime.datetime.strptime(df['Date'][i], '%Y-%m-%d')
#         print(date_obj)
#         print(date_obj.date().isoformat().isocalendar())
#         print()
