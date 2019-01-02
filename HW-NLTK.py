import nltk

nltk.download()
import urllib
#from nltk import word_tokenize
from nltk.book import *
#2
url = "http://www.gutenberg.org/files/863/863-0.txt"
response = urllib.urlopen(url)
raw = response.read().decode('utf8')

#3
raw.find( "CHAPTER I. I GO TO STYLES")
raw.find( "THE END")
raw = raw[939:330289]

#4. Assignment 1F
text_words=string.split(raw)
dictionary={i: 0 for i in set(text_words)}
for word in text_words:
    dictionary[word] += 1
fdist1=FreqDist(text_words)
#lexical_diversity
len(fdist1)/len(text_words)

#5
raw.replace("_", "")
tokens = word_tokenize(raw)
fdist2=FreqDist(tokens)
len(fdist2)/len(tokens)

#6 normalize words
words = [w.lower() for w in tokens]
fdist=FreqDist(words)
#lexical_diversity
len(fdist)/len(text)

#7
wnl = nltk.WordNetLemmatizer()
lemmatized_words=[wnl.lemmatize(t) for t in words]

#8
text = nltk.Text(tokens)
text.concordance("point")

#9
#a.
from nltk.corpus import wordnet as wn
syns=wn.synsets('point')
for i in range(len(syns)):
    print syns[i].definition()
    
#b.
def wordsInSents(text, word):
    li=[]
    sents = nltk.sent_tokenize(text)
    for i in range(len(sents)):
        if word in sents[i]:
            li.append(sents[i])
    return li
print wordsInSents(raw, "point ")

#c
from nltk.wsd import lesk
[lesk(sent, 'point') for sent in wordsInSents(raw, "point ")]

#[lesk(sent, 'point' ) for sent in wordsInSents(raw, "point ")]
#li=wordsInSents(raw, "point ")
for sent in wordsInSents(raw, "point "):
    text=word_tokenize(sent)
    tag=nltk.pos_tag(text)
    #print tag
    li=[v[1] for i, v in enumerate(tag) if v[0] == "point"]
    #print li
    for v in li:
        if v.startswith('J'):
            pos='a'
        elif v.startswith('V'):
            pos='v'
        elif v.startswith('N'):
            pos='n'
        elif v.startswith('R'):
            pos='r'
        else:
            pos=''

        print lesk(sent, 'point', pos)

#10
fdist2.most_common(30) 

#11
li=[(key, value) for key, value in fdist2.iteritems()]   
li=sorted(li, key=lambda x:x[1], reverse=True)

count=0

for i in range(len(fdist2)):

    if li[i][0][0].isalpha():
        print li[i][0],"\t\t", li[i][1]
        count+=1
    if count==30:
        break
