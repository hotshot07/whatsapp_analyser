import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import string

from datetime import date
import calendar
my_date = date.today()
calendar.day_name[my_date.weekday()]

df = pd.read_csv("bhav.csv")


word_list = [str(x) for x in df["Message"]]

tokenized_list = []

for i in word_list:
    sep_wordlist = i.split(sep=' ')
    for word in sep_wordlist:
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


word_list = [x.lower() for x in tokenized_list]

without_stopwords = [word for word in word_list if not word in all_stopwords and not word in string.punctuation]

for lil in Counter(without_stopwords).most_common():
    print(lil[0], lil[1])
