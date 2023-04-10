#Import the requisite library
import spacy

#Sample text
text = "This is a sample number 5555555."
#Build upon the spaCy Small Model
nlp = spacy.blank("en")

#Create the Ruler and Add it
ruler = nlp.add_pipe("entity_ruler")

#List of Entities and Patterns (source: https://spacy.io/usage/rule-based-matching)
patterns = [
                {
                    "label": "PHONE_NUMBER", "pattern": [{"TEXT": {"REGEX": "((\d){5})"}}                                  ]
                }
            ]
#add patterns to ruler
ruler.add_patterns(patterns)

#create the doc
doc = nlp(text)

#extract entities
for ent in doc.ents:
    print (ent.text, ent.label_)