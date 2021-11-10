# Exercise 18:
# Write a program to print the 50 most frequent bigrams (pairs of adjacent words) of a text, omitting bigrams that contain stopwords.

import nltk
import nltk.corpus
from nltk.book import * # program will only run when this line is present...no idea why because it's unrelated
from nltk.corpus import stopwords
stopwords = nltk.corpus.stopwords.words('english')
alice = nltk.corpus.gutenberg.words('carroll-alice.txt')
alice_mod = [w for w in alice if w not in stopwords]
bigrams = nltk.bigrams(alice_mod)
fdist = FreqDist(bigrams)
print(fdist.most_common(50))


# Exercise 19:
# Write a program to create a table of word frequencies by genre, like the one given in 1 for modals. Choose your own words and try to find words whose presence (or absence) is typical of a genre. Discuss your findings.

from nltk.corpus import brown
cfd = nltk.ConditionalFreqDist(
    (genre, word)
    for genre in brown.categories()
    for word in brown.words(categories=genre))
genres = ['hobbies', 'romance', 'mystery', 'news', 'religion', 'science_fiction']
words = ['tools', 'love', 'dead', 'government', 'moral', 'planet']
print(cfd.tabulate(conditions=genres, samples=words))
# I chose each of these words through trial and error to find ones that appear more frequently in one particular genre over another. I'm not sure what else to say about these...they kind of speak for themselves.