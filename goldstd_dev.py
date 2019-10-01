import numpy as np
import pandas as pd
'''
words = []
with open('genia4ertraining/genia4ertask1.iob2','r') as f:
	lines = f.read().splitlines()
	for line in lines:
		if len(line.split())==0:
			continue
		elem = line.strip().split('\t')
		words.append(elem)


goldwords = []
for i in range(0,len(words)):
	if str(words[i][1])=='B':
		if str(words[i+1][1])!='I':
			goldwords.append(str(words[i][0]))
		elif str(words[i+1][1])=='I':
			templist = []
			templist.append(str(words[i][0]))
			for j in range(i+1,len(words)):
				if str(words[j][1])!='I':
					break
				templist.append(str(words[j][0]))
			newterm = str(' '.join(templist))
			goldwords.append(newterm)

goldwords = list(set(goldwords))
count = 0

with open('genia4ertraining/goldstd.txt','w') as f:
	for word in goldwords:
		f.write(str(word)+'\n')

with open('genia4ertraining/unigram_goldstd.txt','w') as f:
	for word in goldwords:
		if len(word.split())==1:
			f.write(str(word)+'\n')

'''
unigram_goldstd = []
with open('genia4ertraining/unigram_goldstd.txt','r') as f:
	for line in f:
		unigram_goldstd.append(line.strip())

corpus = []
with open('genia4ertraining/corpus.raw','r') as f:
	for line in f:
		corpus.append(line.strip())

print(len(set(unigram_goldstd)&set(corpus)))
