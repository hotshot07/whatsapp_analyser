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

    # the most inefficient way possitble to tokenize list :)
    for i in word_list:
        sep_wordlist = i.split(sep=' ')
        for word in sep_wordlist:
            word = word.lower().strip()
            tokenized_list.append(word)

    #add a word to this list to make it not appear in the wordcloud
    custom_list = ['omitted', 'image', "<media", "omitted>", 'hai', "hai", 'nan', 'well', 'spam', 'https', 'Mayank', 'mayank', 'image', 'video', 'message', 'deleted', 'pdf', 'gif', 'deleted',
                   'sticker', "i’ll", "i’m", "Messages", "to", "this", "group", "are", "now", "secured", "with", "to", "end", "end encryption"]

    #adding them hindi stopwords
    all_stopwords = list(stopwords.words('english'))
    hindi_stoplist = open("hindi_stoplist.txt").readlines()
    hindi_stoplist = [i.replace('\n', '') for i in hindi_stoplist]

    #actually a hinglish stoplist
    all_stopwords = hindi_stoplist + custom_list

    without_stopwords = []

    # oh well iterating the list twice
    # should've added the 'check if link' feature in here itself
    for word in tokenized_list:
        if word not in all_stopwords:
            without_stopwords.append(word.lower().strip())

    without_links = []

    links = []

    # saving links for some reason in another list
    # making wordcloud without links as it looks very weird 
    for data in without_stopwords:
        link = re.match(all_links, data)
        if link:
            links.append(link)
        else:
            without_links.append(data)

    with_string = " ".join(without_links)

    # trying to remove a couple of weird characters that keep on appearing
    # can't figure this one out
    with_string = with_string.replace("'re", '')
    with_string = with_string.replace("don", '')

    wordcloud = WordCloud(width=2000, height=1000, min_word_length=3).generate(with_string)
    plt.figure(p_num, figsize=(20, 10), facecolor='k')
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.savefig("output/wordcloud.png")
    return
