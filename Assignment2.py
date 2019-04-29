from collections import Counter
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
#reads content of the file
data_file = open("sourcefiles.txt","r")
wordlist=[]
new_list=[]
new_list1=[]
unique_list=[]
port = PorterStemmer()
lemma= WordNetLemmatizer()
stop_words = set(stopwords.words('english'))
specialcharacters= '.\n\s:"":,-;/*?'


for lines in data_file:
    for words in lines.split():
        wordlist.append(words)
print(wordlist)

for x in wordlist:
    if x in specialcharacters:
        wordlist.remove(x)
        

#wordcount: #function to compute tokens
def wordcount(a):
    count=0
    for element in a:
        count=count+1
    print("The Number of words or tokens in the corpus is ",count)

wordcount(wordlist)

#print unique words #function to compute types

c = Counter(wordlist)
a = [ w for w in wordlist if c[w]==1]
print(a)
print("The number of unique tokens in the corpus is ", wordcount(a))  
#typecount(unique_list,wordlist)

#top 10 frequent words
c1=Counter(wordlist)
frequent_list = c1.most_common(10)
print(frequent_list)

#stopwords
for x  in wordlist:
    if x  not in stop_words:
        new_list.append(x)
print(new_list)

print("After removing StopWords")
wordcount(new_list)
c2 = Counter(new_list)
type_new = [ele for ele in new_list if c2[ele]==1]
wordcount(new_list)
print("Unique Tokens:" )
wordcount(type_new)


stem_list=[]
#stemming
for word in new_list:
    stem_list.append(port.stem(word))
print(stem_list)
wordcount(stem_list)
c3 = Counter(stem_list)
new_stem=[i for i in stem_list if c3[i]==1]
print("After Stemming")
wordcount(stem_list)
print("Unique tokens:")
wordcount(new_stem)

#lemmatization
lemma_list =[]
for word in new_list:
    lemma_list.append(lemma.lemmatize(word))

print(lemma_list)
print("After Lemmatization")
wordcount(lemma_list)

c4 = Counter(lemma_list)
lemma_list_unique = [ z for z in lemma_list if c4[z]==1]
wordcount(lemma_list_unique)




    
    
