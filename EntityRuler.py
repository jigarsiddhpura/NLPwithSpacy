import spacy

text = "West Chestertenfieldville was refrenced in Mr. Deeds."

nlp = spacy.load("en_core_web_sm")
ruler = nlp.add_pipe("entity_ruler")

# print(nlp.analyze_pipes())

# ADDIND CUSTOM FEATURES IN SPACEY PIPELINE (RULE BASED APPROACH) 📌📌
# adding when there is TOPONYM RESOLUTION
patterns = [
    {'label':'ULLU', 'pattern':'West Chestertenfieldville'},
    {'label':'FILM', 'pattern':'Mr. Deeds'}
]
ruler.add_patterns(patterns)
doc = nlp(text)

for ent in doc.ents:
    print(ent.text, ent.label_)


nlp2 = spacy.load("en_core_web_sm")
# before="ner" bcz without it , we cannot change the entity type assign by it. ⭐⭐
ruler = nlp2.add_pipe("entity_ruler", before="ner")
ruler.add_patterns(patterns)
doc2 = nlp2(text)
for ent in doc2.ents:
    print(ent.text, ent.label_)

