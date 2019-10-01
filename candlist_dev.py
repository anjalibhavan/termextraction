import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import csv
import string
from nltk.corpus import stopwords
from lxml import etree
from xml.etree import cElementTree as ET

eng_stop_words = list(set(stopwords.words('english')))
with open('genia4ertraining/long_stopwords.txt','r') as fin:
    long_stop_words = set(fin.read().splitlines())

stop_words = set(eng_stop_words).union(set(long_stop_words))

def int_filter( someList ):
    for v in someList:
        try:
            if int(v):
                continue
        except ValueError:
            yield v

words = []
with open('genia4ertraining/corpus.raw','r') as f:
    line = f.read().splitlines()
    for i in line:
        if len(i.split())==0:
            continue
        words.append(i)

print(len(words))
words = [x for x in words if x not in string.punctuation and x.lower() not in stop_words]


words = list(set(words))
print(len(words))

with open('genia4ertraining/unis.txt','w') as f:
    for word in words:
        f.write(str(word)+'\n')

