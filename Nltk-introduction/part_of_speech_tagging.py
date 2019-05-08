"""Part of speech tagging tool with PunktSentenceTokenizer and gutenberg corpus"""

import nltk
from nltk.corpus import gutenberg # One of corpusses
from nltk.tokenize import PunktSentenceTokenizer # Unsupervised learning tokenizer, already trained

train_text = gutenberg.raw("whitman-leaves.txt")
sample_text = ("I saw the best minds of my generation destroyed by madness,\
               starving hysterical naked, dragging themselves through the negro streets at dawn\
               looking for an angry fix angelheaded hipsters burning for the ancient\
               heavenly connection to the starry dynamo in the machinery of the night.")

print (gutenberg.raw("whitman-leaves.txt")[0:460]) # Sample of Whitman's corpus

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content(): # Function for tagging part of speech
    try:
        for i in tokenized[:5]:
            words = nltk.word_tokenize(i) # Identifies the tokens
            tagged = nltk.pos_tag(words) # Part of speech tagger from nltk library 
            print(tagged)

    except Exception as e:
        print(str(e))
 
process_content()

#print (nltk.help.upenn_tagset()) uncomment this to see legend for taggs
