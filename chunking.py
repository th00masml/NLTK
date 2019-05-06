"""Chunking script for Ginsberg's quotes"""

import numpy as np
import nltk
from nltk.tokenize import word_tokenize

ginsberg_array_long =["who threw their watches off the roof to cast their ballot for an Eternity outside of Time,\
               and alarm clocks fell on their heads every day for the next decadey"]


ginsberg_array_short = ['Follow your inner moonlight; do not hide the madness.']
               
# Let's try the program with simple quote from Allen Ginsberg

def processContent_chunked_short():
    try:
        for item in ginsberg_array_short:
            tokenized = nltk.word_tokenize(item)
            tagged = nltk.pos_tag(tokenized)

            chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}""" # any adverb 0 or more, verb 0 or more, proper noun 0 or more and the same with noun
            chunkParser = nltk.RegexpParser(chunkGram)

            chunked = chunkParser.parse(tagged)
            print(chunked)
            chunked.draw()
            
    except Exception as e:
        print(str(e))
    
print (processContent_chunked_short())

# Now, let's try with something longer, also written by Ginsberg. 
# You need to close processContent_chunked_short diagram, to see this one

def processContent_chunked_long():
    try:
        for item in ginsberg_array_long:
            tokenized = nltk.word_tokenize(item)
            tagged = nltk.pos_tag(tokenized)

            chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""# any adverb 0 or more, verb 0 or more, proper noun 0 or more and the same with noun
            chunkParser = nltk.RegexpParser(chunkGram)

            chunked = chunkParser.parse(tagged)
            print(chunked)
            chunked.draw()
            
    except Exception as e:
        print(str(e))
    
print (processContent_chunked_long())