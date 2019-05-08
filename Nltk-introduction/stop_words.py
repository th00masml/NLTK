"""Simple script deleting stop words from quote"""
    
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sent = "If people never did silly things nothing intelligent would ever get done"

stop_words = set(stopwords.words('english'))
# print (stop_words) uncomment it to see all stopwords for english language

word_tokens = word_tokenize(example_sent)

filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)
        
# filtered_sentence = [w for w in word_tokens if not w in stop_words] alternative, shorter version of loop

print("Word tokens are:", word_tokens)
print("And here is sentence without stopwords:", filtered_sentence)
