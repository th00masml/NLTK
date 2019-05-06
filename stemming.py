"""Simple stemming tool"""

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()
example_words = ["swim", "swimmer", "swimming"] # Simple steamming example

for w in example_words:
    print(ps.stem(w))
    
text_to_steam = ("The problems are solved, not by giving new information,\
                 but by arranging what we have known since long.") # Longer text. Let's see how script will handle it

words = word_tokenize(text_to_steam) # Assigning example text from variable to word tokenizer
for w in words:
    print("Stemmed word is:", ps.stem(w)) # Printing the result with comment