import numpy as np
import pandas as pd
from wordcloud import WordCloud
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import re

import warnings
warnings.filterwarnings("ignore")

# youtube_regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$"


def make_wordcloud(p_num):
    all_links = r"^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$"

    df = pd.read_csv("userdata/chat.csv")

    word_list = [str(x) for x in df["Message"]]

    tokenized_list = []

    for i in word_list:
        sep_wordlist = i.split(sep=' ')
        for word in sep_wordlist:
            word = word.lower().strip()
            tokenized_list.append(word)

    custom_list = ['omitted', 'image', "<media", "omitted>", 'hai', 'nan', 'well', 'spam', 'https', 'Mayank', 'mayank', 'image', 'video', 'message', 'deleted', 'pdf', 'gif', 'deleted',
                   'sticker', "i’ll", "i’m", "Messages", "to", "this", "group", "are", "now", "secured", "with", "to", "end", "end encryption"]

    all_stopwords = list(stopwords.words('english'))
    hindi_stoplist = open("hindi_stoplist.txt").readlines()
    hindi_stoplist = [i.replace('\n', '') for i in hindi_stoplist]

    all_stopwords = hindi_stoplist + custom_list

    without_stopwords = []

    for word in tokenized_list:
        if word not in all_stopwords:
            without_stopwords.append(word.lower().strip())

    without_links = []

    links = []

    for data in without_stopwords:
        link = re.match(all_links, data)
        if link:
            links.append(link)
        else:
            without_links.append(data)

    with_string = " ".join(without_links)

    with_string = with_string.replace("'re", '')
    with_string = with_string.replace("don", '')

    wordcloud = WordCloud(width=2000, height=1000, min_word_length=3).generate(with_string)
    plt.figure(p_num, figsize=(20, 10), facecolor='k')
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.savefig("output/wordcloud.png")
    return 1
