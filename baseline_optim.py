import re
import numpy as np
from scipy import sparse
import pandas as pd
import collections
from tfidf_calculator import computeTF, computeIDF, computeTFIDF
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer, TfidfTransformer
import nltk

sentence_list = []
with open('genia4ertraining/tokenized_sentences.txt','r',encoding='utf-8') as f:
	lines = f.read().rstrip().split('\n')
	for line in lines:
		if len(line.split())==0:
			continue
		sentence_list.append(line.strip())

candidates = []
with open('genia4ertraining/unigram_candidates.txt','r') as f:
	for word in f:
		candidates.append(word.strip())
print(len(candidates))
candidates = list(sorted(set(candidates)))

bowlist = []
for sent in sentence_list:
	bowlist.append(sent.split())

indices = []
for i in range(0,len(candidates)):
	indices.append(i)

unis = dict(zip(candidates,indices))

tfmatrix = computeTF(unis,bowlist,sentence_list)

vectorizer = TfidfTransformer()
res = vectorizer.fit_transform(tfmatrix).todense()

finalsums = np.array(np.sum(res,axis=0))
with open('genia4ertraining/finalsums.txt','w',encoding='utf-8') as f:
	for i in range(0,len(candidates)):
			f.write(str(finalsums[0][i])+'\n')

with open('genia4ertraining/unigram_candidates.txt','w',encoding='utf-8') as f:
	for i in range(0,len(candidates)):
			f.write(str(finalsums[0][i])+'\n')