import numpy as np
import pandas as pd
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from nltk.corpus import stopwords
import string
import matplotlib.pyplot as plt
import re

import warnings
warnings.filterwarnings("ignore")

youtube_regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$"

all_links = r"^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$"

df = pd.read_csv("userdata/chat.csv", index_col=0)


word_list = [str(x) for x in df["Message"]]

tokenized_list = []

for i in word_list:
    sep_wordlist = i.split(sep=' ')
    for word in sep_wordlist:
        word = word.lower().strip()
        tokenized_list.append(word)


all_stopwords = stopwords.words('english')
all_stopwords.append('omitted')
all_stopwords.append('image')
all_stopwords.append('h')
all_stopwords.append('nan')
all_stopwords.append('well')
all_stopwords.append('spam')
all_stopwords.append('https')
all_stopwords.append('Mayank')
all_stopwords.append('mayank')
all_stopwords.append('image')
all_stopwords.append('video')
all_stopwords.append('message')
all_stopwords.append('deleted')
all_stopwords.append('pdf')
all_stopwords.append('gif')
all_stopwords.append('deleted')
all_stopwords.append('sticker')
all_stopwords.append('re')
all_stopwords.append("i’ll")
all_stopwords.append("i’m")

hindi_stoplist = open("hindi_stoplist.txt").readlines()
hindi_stoplist = [i.replace('\n', '') for i in hindi_stoplist]

all_stopwords.append(hindi_stoplist)

without_stopwords = [word for word in tokenized_list if not word in all_stopwords]

without_links = []

links = []

for data in without_stopwords:
    link = re.match(all_links, data)
    if link:
        links.append(link)
    else:
        without_links.append(data)

with_string = " ".join(without_links)

wordcloud = WordCloud(width=1600, height=800).generate(with_string)
plt.figure(figsize=(20, 10), facecolor='k')
plt.axis("off")
plt.imshow(wordcloud, interpolation='bilinear')
plt.tight_layout(pad=0)
plt.show()
