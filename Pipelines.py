import spacy
from spacy import displacy
import numpy as np

# creating blank spacy pipeline
nlp = spacy.blank('en')
nlp.add_pipe("sentencizer")
print(nlp.analyze_pipes())

print("---------------------")
print("---------------------")

nlp2 = spacy.load('en_core_web_sm')
print(nlp2.analyze_pipes())

