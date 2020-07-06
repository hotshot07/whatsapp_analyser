import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
import copy


def user_activity_vis(p_num):
    df = pd.read_csv("userdata/chat.csv", index_col=0)

    # df = df[~df['User'].isin(['added'])]
    # removing top 3 rows (like when this group was created) and all
    df_user = df['User'].iloc[3:].value_counts()

    # this shows up in username thanks to my excellent parsing skills
    del_list = ["added", "You", "left"]

    df_user2 = copy.deepcopy(df_user)

    # oh why not just pass when an exception occurs?
    for key, value in df_user2.items():
        str_key = list(key.strip().split())
        for word in str_key:
            if word in del_list:
                try:
                    del df_user[key]
                except:
                    pass

    plt.figure(p_num, figsize=(len(df_user) + 3, 6))
    week_chart = sns.barplot(df_user.index, df_user.values, alpha=0.8, palette='rocket')
    plt.xlabel('Users', fontsize=12, fontname="Andale Mono")
    plt.ylabel('Total messages sent', fontsize=12, fontname="Andale Mono")
    plt.title('User activity', fontsize=14, fontname="Andale Mono")
    week_chart.set_xticklabels(week_chart.get_xticklabels(), rotation=90, fontweight='light', horizontalalignment='center', fontsize=6)
    plt.tight_layout()
    plt.savefig("output/user_activity.png")
    return 1
