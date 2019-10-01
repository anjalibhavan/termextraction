import numpy as np
import pandas as pd
import re
from chardet import detect
import random
import os
import itertools
from random_sampling import random_sampling
import matplotlib.pyplot as plt
from pprint import pprint

goldwords = []
#with open('goldstd_big.txt','r') as f:
with open('goldwords_small.txt','r') as f:
    line = f.read().rstrip().splitlines()
    for elem in line:
        if len(elem.split())==1:
            goldwords.append(elem)

newlist = []
#with open('tokenized_sentences_big.txt','r',encoding = 'utf-8') as f:
with open('4ersample_small.raw','r') as f:
    newlist = f.read().splitlines()

parlist = []
for i in range(0,len(newlist)):
    parlist.append(newlist[i].split(' '))
parlist = list(itertools.chain.from_iterable(parlist))
print(len(parlist))

term_counts = []
corpus_sizes = []

for i in range(1,len(parlist)+1):
    corpus_sizes.append(i)

for i in corpus_sizes:
    countarr = []
    for j in range(0,5):
        count = 0
        bow = random_sampling(parlist,i)
        for word in bow:
            if word in goldwords:
                count+=1
        countarr.append(count)
    term_counts.append(sum(countarr)/float(len(countarr)))

plt.plot(corpus_sizes,term_counts)
plt.show()
#print(np.polyfit(corpus_sizes,term_counts,deg=1))
