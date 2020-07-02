import numpy as np
import pandas as pd
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from nltk.corpus import stopwords
import string
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv("userdata/chat.csv", index_col=0)


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
all_stopwords.append('re')
all_stopwords.append('ll')


word_list = [x.lower() for x in tokenized_list]

hindi_stoplist = open("hindi_stoplist.txt").readlines()
hindi_stoplist = [i.replace('\n', '') for i in hindi_stoplist]

without_stopwords = [word.lower() for word in word_list if not word in all_stopwords and not word in string.punctuation and not word in hindi_stoplist]

print(without_stopwords)

# for lil in Counter(without_stopwords).most_common(50):
#     print(lil[0], lil[1])
# Create and generate a word cloud image:
with_string = " ".join(without_stopwords)
wordcloud = WordCloud(width=1600, height=800).generate(with_string)
plt.figure(figsize=(20, 10))
# # Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')

plt.axis("off")
plt.show()
