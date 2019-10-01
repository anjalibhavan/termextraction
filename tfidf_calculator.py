import numpy as np
import math
from scipy import sparse
import pandas as pd
from operator import itemgetter
from sklearn.feature_extraction.text import TfidfVectorizer

def computeTF(unis,bowlist,sentence_list):
    count = 0
    tfmatrix = np.zeros((len(sentence_list),len(unis)))
    for i in range(0,len(sentence_list)):
        bowCount = len(bowlist[i])
        for j in range(0,bowCount):
            if bowlist[i][j] in unis.keys():
                tfmatrix[i][unis[bowlist[i][j]]]+=1/float(bowCount)
    return sparse.csr_matrix(tfmatrix)


def computeIDF(docList,unigrams,tfmatrix):
    count = 0
    idf_values = {}
    N = len(docList)
    idf_values = dict.fromkeys(unigrams, 0)
    for i in range(0,len(docList)):
       for j in range(0,len(unigrams)):
        if tfmatrix[i][j]==0:
            idf_values[unigrams[j]]=1
        else:
            idf_values[unigrams[j]]+=1

    for word, val in idf_values.items():
        idf_values[word] = math.log10(N / float(val))
    print(len(idf_values))
    return idf_values


def computeTFIDF(tfmatrix, idf_values,unigrams):
    tfidfmatrix = np.zeros_like(tfmatrix)
    for i in range(0,tfmatrix.shape[0]):
        for j in range(0,tfmatrix.shape[1]):
            tfidfmatrix[i][j] = tfmatrix[i][j]*idf_values[unigrams[j]]
    return tfidfmatrix



'''
I want to avoid using the following nested loop:

    for i in range(0,tfmatrix.shape[0]):
        for j in range(0,tfmatrix.shape[1]):
              if tfmatrix[i][j]==0:
                     #change value in idf_values to 1 
              else:
                    #incremenet value in idf_values

The reason is that the matrix is enormous, and running this for loop is not possible in any reasonable amount of time. `idf_values` is where I want to modify values in case the elements in the matrix are zero or nonzero, accordingly.


'''