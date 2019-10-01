import spacy
from pprint import pprint
import nltk
import string
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import tree2conlltags, conlltags2tree
from ast import literal_eval as make_tuple
from spacy import displacy
from collections import Counter
import en_core_web_sm


nlp = en_core_web_sm.load()
nlp.max_length = 4000000
sentences = []

with open('genia4ertraining/tokenized_sentences.txt','r') as f:
	sentences = f.read().splitlines()

doc = []
for sent in sentences:
	doc.append(nlp(sent))

entities = []
for sent in doc:
	for X in sent.ents:
		tup = X.text
		#pprint(tup)
		entities.append(tup)
with open('genia4ertraining/ner.txt','w') as f:
	for i in entities:
		f.write(str(i)+'\n')

'''
tags = []
with open('genia4ertraining/results.txt','r') as f:
	lines = f.read().rstrip().splitlines()
	for tup in lines:
		if len(tup)==0:
			continue
		tags.append(tup)

newtags = []
for i in range(0, len(tags)):
	newtags.append(tags[i].replace('\x00',''))

finaltags = []
count = 0
for i in range(0,len(newtags)):
	if len(newtags[i])==0:
		continue
	finaltags.append(tuple(newtags[i].strip('()').split(',')))

with open('genia4ertraining/nerresults.txt','w') as f:
	for tup in finaltags:
		f.write(str(tup)+'\n')
pprint(finaltags[0:10])
'''
'''
with open('genia4ertraining/nerresults.txt','r') as f:
	docs = f.read().splitlines()

newdocs = []
for i in range(0,len(docs)):
	elem = list(docs[i].strip('()').split(','))
	elem = [i.replace("'", '') for i in elem]
	newdocs.append(elem)

finaldocs = []
print(len(newdocs))
for tup in newdocs:
	if tup[2]!=' ':
		finaldocs.append(tup)

print(len(finaldocs))
with open('genia4ertraining/nertags.txt','w') as f:
	for tup in finaldocs:
		f.write(str(tup)+'\n')

print(finaldocs[0])

'''
'''
fdocs = []
with open('genia4ertraining/nertags.txt','r') as f:
	lines = f.read().splitlines()
	for line in lines:
		if len(line.split())==0:
			continue
		fdocs.append(line)

with open('genia4ertraining/nertags.txt','w') as f:
	for tup in fdocs:
		f.write(str(tup)+'\n')
'''