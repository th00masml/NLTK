"""Simple program for tokenizing words in given sentence from Wittgenstein"""

from nltk.tokenize import sent_tokenize, word_tokenize

example_text = "To imagine a language is to imagine a form of life."

print(sent_tokenize(example_text))
print(word_tokenize(example_text))

for i in word_tokenize(example_text):
    print (i)
