# Exercise 24:

from nltk.book import * # Imports NLTK texts
# Searches the text for each of the following criteria:
words1 = [w for w in set(text6) if w.endswith('ise')]
words2 = [w for w in set(text6) if 'z' in w]
words3 = [w for w in set(text6) if 'pt' in w]
words4 = [w for w in set(text6) if w.istitle()]
# Prints each of the lists
print(words1)
print(words2)
print(words3)
print(words4)


# Exercise 25:

sent = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore'] # Establishes list
# Searches for 'sh' words in text:
sh_words = [w for w in sent if w.startswith('sh')]
# Searches for words longer than 4 characters in text:
long_words = [w for w in sent if len(w) > 4]
# Prints both outputs
print(sh_words)
print(long_words)