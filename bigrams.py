with open('genia4ertraining/goldstd.txt','r') as f:
	goldwords = [word.strip() for word in f]
bigrams = []
unigrams = []
for term in goldwords:
	if len(term.split())==2:
		bigrams.append(term)
	elif len(term.split())==1:
		unigrams.append(term)

with open('genia4ertraining/bigram_goldstd.txt','w') as f:
	for term in bigrams:
		f.write(term+'\n')

with open('genia4ertraining/unigram_goldstd.txt','w') as f:
	for term in unigrams:
		f.write(term+'\n')