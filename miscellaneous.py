
parser = etree.XMLParser(recover=True)

doc = etree.parse('C:/users/anjali/environments/termextraction/GENIA_term_3.02/GENIAcorpus3.xml',parser)
print(doc)
constis = doc.find('cons')
print(constis)
with open('constis.txt','a') as fout:
    fout.write(constis+'\n')

with open('GENIA_term_3.02/GENIAcorpus3.xml') as f:
    xmlstr=f.read()
    #xmlDocTree = ET.XML(xmlstr)
soup = BeautifulSoup(xmlstr, "html.parser")
required0 = soup.find_all("cons")
title = []
for i in required0:
    title.append(i.get_text())
with open('constis.txt','a') as fout:
    for constis in title:
        fout.write(constis+'\n')
#print(title)

for line in docs:
    if len(line.split()) == 0:
        continue
    #elements = line.strip().split('\t')
    words.append(line)

with open('4ersample.txt','r') as f:
    line = f.read().splitlines()
    for i in line:
        element = i.strip().split('\t')
        words.append(element)

'''

tfidfbow = []
for i in range(0,10):
    tfidfbow.append(computeTFIDF(tfbow[i],idfs))

df = pd.DataFrame(tfidfbow)
newdf = df.sum(axis = 0)
newdf = newdf.sort_values(ascending = False)

names = list(newdf.index.values)
newlist = list(zip(names,newdf.iloc[:]))
predstemp = []
for i in range(0,len(newlist)):
    predstemp.append(list(newlist[i]))
    

def allot(predstemp,N):
    preds = predstemp
    count = 0
    for i in range(0,len(predstemp)):
        if count<N:
            preds[i][1] = 1
        else:
            preds[i][1] = 0
        count+=1
    return preds

preds = allot(predstemp,300)

wrds = []

with open('4ersample.txt','r') as f:
    lines = f.read().splitlines()
    for i in lines:
        element = i.strip().split('\t')
        wrds.append(element)

predsfinal = sorted(preds, key=lambda tup: tup[0])
testfinal = sorted(wrds, key=lambda tup: tup[0])

preds = []
test = []
count = 0
for tup in predsfinal:
    if count<735:
        preds.append(tup[1])
        count+=1
for tup in testfinal:
    test.append(int(tup[1]))

preds = np.array(preds)
test = np.array(test)
'''

'''
sentarr = []
for i in range(0,len(sentence_list)):
    sentarr.append(str(i))
worddict = makehash()

for i in range(0,len(sentence_list)):
    for word in unigrams:
        worddict[str(i)][word] = 0

for i in range(0,len(sentence_list)):
    for word in unigrams:
        for bow in bowlist[i]:
            if bow==word:
                worddict[str(i)][word]+=1
print(worddict['0']['requires'])


#calctf
tfbow = []
for i in range(0,len(sentence_list)):
tfbow.append(computeTF(worddict[i],bowlist[i]))

#calcidf
idfs = computeIDF(worddict)

#calctfidf
tfidfbow = []
for i in range(0,len(sentence_list)):
tfidfbow.append(computeTFIDF(tfbow[i],idfs))

newlist = list(zip())




'''



count = 0
for i in range(0,vocab_len):
    score[i]=1
    for j in range(0,vocab_len):
        if j==i:
            weighted_edge[i][j]=0
        else:
            for window_start in range(0,(len(bowlist)-window_size)):
                
                window_end = window_start+window_size
                
                window = bowlist[window_start:window_end]
                if (candidates[i] in window) and (candidates[j] in window):
                    index_of_i = window_start + window.index(bowlist[i])
                    index_of_j = window_start + window.index(bowlist[j])
                    
        
                    if [index_of_i,index_of_j] not in covered_coocurrences:
                        weighted_edge[i][j]+=1/math.fabs(index_of_i-index_of_j)
                        covered_coocurrences.append([index_of_i,index_of_j])