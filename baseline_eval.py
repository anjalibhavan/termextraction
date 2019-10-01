import numpy as np
from pprint import pprint
import matplotlib.pyplot as plt
import pandas as pd

candidates = []
with open('genia4ertraining/unigram_candidates.txt','r') as f:
	for word in f:
		candidates.append(word.strip())
#candidates = list(sorted(candidates))

finalsums = []
with open('genia4ertraining/finalsums.txt','r') as f:
	for line in f:
		finalsums.append(float(line.strip()))

goldwords = []
with open('genia4ertraining/unigram_goldstd.txt','r') as f:
	for word in f:
		goldwords.append(word.strip())

count = 0
for i in range(0,len(finalsums)):
	if finalsums[i]==0 or finalsums[i]==0.0:
		count+=1
print(count)

scores = list(zip(candidates,finalsums))
for tup in scores:
	if tup[1]==0 or tup[1]==0.0:
		pprint(tup)
		
scoresfinal = sorted(scores, key=lambda tup: tup[1],reverse=True)
pruned_terms = scoresfinal[0:857]
#pprint(pruned_terms)
gold_len = len(goldwords)
pruned_len = len(pruned_terms)

res = 0
for tup in pruned_terms:
	if str(tup[0]) in goldwords:
		res+=1

precision = res/pruned_len
recall = res/gold_len
#print(res)
print('precision', precision)
print('recall', recall)
print('f1',2*precision*recall/(precision+recall))
'''
x = [10,20,50,100,500,1000,1800,2000,5000,10000,15000,20000]
y_p = []
y_r = []
for i in x:
	pruned_new = scoresfinal[0:i]
	pruned_new_len = len(pruned_new)
	res = 0
	for tup in pruned_new:
		if str(tup[0]) in goldwords:
			res+=1
	y_p.append(res/pruned_new_len)
	y_r.append(res/gold_len)

plt.plot(x,y_p)
plt.show()
plt.plot(x,y_r)
plt.show()
'''




