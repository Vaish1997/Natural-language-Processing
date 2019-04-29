#reading contents of the file into the list:
import nltk
import string
from collections import Counter

#program
wordlist =[]
data_file= open("sourcefiles.txt","r")
for lines in data_file:
    for words in lines.split():
        wordlist.append(words)
print("words in the corpus")
print(wordlist)

#removepunctuations

t = str.maketrans("", "", string.punctuation)
for x in wordlist:
    x.translate(t)
print(wordlist)
count = Counter(wordlist)
print(count)

#unigram
countlist = []
countlist = list(count.values())
unigramprob = []
prob = 0
for x in countlist:
    prob = (x/len(wordlist))* (10**2)
    prob = round(prob,5)
    unigramprob.append(prob)

c = Counter(unigramprob)

unigramdict = {}

for x in wordlist:
    for y in unigramprob:
        unigramdict[x] = y
print("words and their probabilities in the corpus")
print(unigramdict)

#Top fifteen unigram probabilities:
mostFreq = c.most_common(15)
print(mostFreq)

#trying two different corpus:

modified_length = len(wordlist)//2

corpus1 = []
corpus2 = []
corpus1  = wordlist[0 : modified_length]
corpus2 = wordlist[modified_length :]
print(corpus1)
print(corpus2)

corpus1count = Counter(corpus1)
corpus2count = Counter(corpus2)

corpus1list = []
corpus2list = []
unigramprob1 =[]
unigramprob2 =[]

prob =0;
corpus1list = list(corpus1count.values())
corpus2list = list(corpus2count.values())

for x in corpus1list:
    prob = (x/len(corpus1))* (10**2)
    prob = round(prob,5)
    unigramprob1.append(prob)
c2 =Counter(unigramprob1)
mostfreq1 = c2.most_common(15)
print("Most frequent in corpus1")
print(mostfreq1)
prob = 0
for x in corpus2list:
    prob = (x/len(corpus2))* (10**2)
    prob = round(prob,5)
    unigramprob2.append(prob)

c3 =Counter(unigramprob2)
mostfreq2 = c3.most_common(15)
print("Most frequent in corpus2")
print(mostfreq2)

unigramdict1 = {}
unigramdict2 = {}

for x  in corpus1:
    for  y in unigramprob1:
        unigramdict1[x] = y
print("unigram probability in the corpus1")
print(unigramdict1)

for x  in corpus2:
    for  y in unigramprob2:
        unigramdict2[x] = y
print("unigram probabillity in the corpus 2")
print(unigramdict2)

#bigram
bi = list(nltk.bigrams(wordlist))

print(" list of bigrams")
print(bi)



#bigrams in two different corpuses
bigram1 = list(nltk.bigrams(corpus1))
bigram2 = list(nltk.bigrams(corpus2))

print("bigrams in corpus1")
print(bigram1)
print("Bigrams in corpus2")
print(bigram2)


