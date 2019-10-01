import numpy as np
import pandas as pd

with open('genia4ertraining/ner.txt','r') as f:
	ners = f.read().splitlines()

with open('genia4ertraining/goldstd.txt','r') as f:
	goldwords = f.read().splitlines()

nerlen = len(ners)
goldlen = len(goldwords)
print(nerlen)
print(goldlen)
termcount = 0
for word in ners:
	if word in goldwords:
		termcount+=1
print(termcount)
print('precision',termcount/nerlen)
print('recall',termcount/goldlen)

