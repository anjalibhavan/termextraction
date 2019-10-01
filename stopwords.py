import nltk
import string
from nltk import word_tokenize
from collections import Counter
import os
from chardet import detect
from nltk.corpus import stopwords
import numpy as np
from nltk.util import ngrams
import pandas as pd
import scipy

def get_encoding_type(file):
	with open(file, 'rb') as f:
		rawdata = f.read()
	return detect(rawdata)['encoding']


rootdir = 'C:/Users/anjali/desktop/nptel/'
stop_words = set(stopwords.words('english'))
print(stop_words)

#docs=[]
for file_name in os.listdir(rootdir):
	froot="".join(file_name)
	root_dir=rootdir+froot+'/'
	docs=[]
	for filename in os.listdir(root_dir):
		if filename[3]=='n':
			name = "".join(filename)
			full_name = root_dir+name
			from_codec = get_encoding_type(full_name)
			with open(full_name, 'r', encoding=from_codec) as f, open('trgfile.txt', 'w', encoding='utf-8') as e:
				text = f.read() # for small files, for big use chunks
				e.write(text)
			
			os.remove(full_name) # remove old encoding file
			os.rename('trgfile.txt', full_name) # rename new encoding
			f1 = open(full_name,encoding='utf8')
			doc = f1.read()
			docs.append(doc)
		
	docs = (' '.join(filter(None, docs))).lower()
	tokens = word_tokenize(docs)
	tokens = [t.lower() for t in tokens if t not in stop_words and t not in string.punctuation]
	unigrams = list(ngrams(tokens,1))
	c = Counter(unigrams)
	docstopwords = [x[0][0] for x in c.most_common(100)]

	for filename in os.listdir(root_dir):
		if filename[3]=='n':
			name = "".join(filename)
			full_name = root_dir+name
			f = open(full_name,encoding='utf8')
			doc = f.read().split()
			words = [words.lower() for words in doc if words not in stop_words]
			with open(full_name,'w',encoding='utf8') as fout:
				fout.write(" ".join(words))

		
print('done')





'''
docs = (' '.join(filter(None, docs))).lower()
tokens = word_tokenize(docs)
postokens = nltk.pos_tag(tokens)

tokens = [t for t in tokens if t not in stop_words and t not in string.punctuation]


bigrams = list(ngrams(tokens,2))

c = Counter(bigrams)
docstops = [x[0] for x in c.most_common(100)]
docstopwords=[]

for tupes in docstops:
	docstopwords.append( (''.join([w+' ' for w in tupes])).strip())
print(docstopwords)

def neighbors(mylist):
	i = 0
	while i+1 < len(mylist):
		yield (mylist[i], mylist[i + 1])
		i += 1

for filename in os.listdir(root_dir):
	if filename[3]=='n':
		name = "".join(filename)
		full_name = root_dir+name
		f = open(full_name,encoding='utf8')
		doc = f.read().split()
		words = [words for words,y in neighbors(doc) if words+' '+y not in docstopwords and words not in string.punctuation and y not in string.punctuation]
		with open(full_name,'w',encoding='utf8') as fout:
			fout.write(" ".join(words))
print('done')
'''
'''
c = Counter(unigrams)
docstopwords = [x[0][0] for x in c.most_common(100)]

for filename in os.listdir(root_dir):
	if filename[3]=='n':
		name = "".join(filename)
		full_name = root_dir+name
		f = open(full_name,encoding='utf8')
		doc = f.read().split()
		words = [words for words in doc if words not in docstopwords and words not in string.punctuation]
#UTF-8-SIG Windows-1252
		
		with open(full_name,'w',encoding='utf8') as fout:
			fout.write(" ".join(words))
			
'''

