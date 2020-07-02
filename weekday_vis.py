import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import calendar
from dateutil import parser
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv("userdata/chat.csv", index_col=0)

day_list = []
for i in range(len(df['Date'])):
    my_date_str = str(df['Date'][i]) + ' ' + str(df['Time'][i])
    try:
        datetime_obj = parser.parse(my_date_str)
        day_list.append(calendar.day_name[datetime_obj.weekday()])
    except:
        day_list.append(np.nan)


df['Day'] = day_list

df_day = df['Day'].value_counts()

order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

sns.barplot(df_day.index, df_day.values, alpha=0.8, palette='rocket', order=order)

plt.show()
