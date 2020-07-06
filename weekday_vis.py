import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

# no brainer
def make_week_vis(p_num):
    df = pd.read_csv("userdata/chat.csv", index_col=0)

    df_day = df['Day'].value_counts()

    order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    plt.figure(p_num, figsize=(8, 4))
    week_chart = sns.barplot(df_day.index, df_day.values, alpha=0.8, palette='rocket', order=order)
    plt.xlabel('Days of the week', fontsize=12, fontname="Andale Mono")
    plt.ylabel('Messages exchanged', fontsize=12, fontname="Andale Mono")
    plt.title('Day wise chat activity', fontsize=14, fontname="Andale Mono")
    plt.tight_layout()
    plt.savefig("output/week_vis.png")
    return
