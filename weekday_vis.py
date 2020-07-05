import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv("userdata/chat.csv", index_col=0)

df_day = df['Day'].value_counts()

order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


sns.barplot(df_day.index, df_day.values, alpha=0.8, palette='rocket', order=order)
plt.xlabel('Weekdays', fontsize=18, fontname="Andale Mono")
plt.ylabel('Messages', fontsize=16, fontname="Andale Mono")
plt.title('Chat Activity', fontsize=20, fontname="Andale Mono")

plt.show()
