import numpy as np
import pandas as pd
from wordcloud import WordCloud
#from nltk.corpus import stopwords
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

    # creating a list of strings of individual words of the messages
    for i in word_list:
        sep_wordlist = i.split(sep=' ')
        for word in sep_wordlist:
            word = word.lower().strip()
            tokenized_list.append(word)

    # add a word to this list to make it NOT appear in the wordcloud
    custom_list = ['omitted', 'image', "<media", "omitted>", 'hai', "hai", 'nan', 'well', 'spam', 'https', 'Mayank', 'mayank', 'image', 'video', 'message', 'deleted', 'pdf', 'gif', 'deleted',
                   'sticker', "document", "i’ll", "i’m", "Messages", "to", "this", "group", "are", "now", "secured", "with", "to", "end", "end encryption"]

    english_stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he',
                         'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it',
                         "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what',
                         'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are',
                         'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did',
                         'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of',
                         'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before',
                         'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under',
                         'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where',
                         'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other',
                         'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too',
                         'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now',
                         'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't",
                         'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven',
                         "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn',
                         "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't",
                         'won', "won't", 'wouldn', "wouldn't"]

    # adding them hindi stopwords
    hindi_stoplist = open("hindi_stoplist.txt").readlines()
    hindi_stoplist = [i.replace('\n', '') for i in hindi_stoplist]

    # actually a hinglish stoplist now
    all_stopwords = english_stopwords + hindi_stoplist + custom_list

    without_stopwords = []

    # oh well iterating the list twice in two loops below
    # should've added the 'check if link' feature in here itself
    for word in tokenized_list:
        if word not in all_stopwords:
            without_stopwords.append(word.lower().strip())

    without_links = []

    links = []

    # saving links for some reason in another list (next feature maybe?)
    # making wordcloud without links as it looks very weird
    for data in without_stopwords:
        link = re.match(all_links, data)
        if link:
            links.append(link)
        else:
            without_links.append(data)

    # wordcloud only accepts string as input
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


# Testing
# if __name__ == '__main__':
#     make_wordcloud(2)
