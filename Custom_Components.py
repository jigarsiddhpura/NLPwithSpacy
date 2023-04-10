import spacy
from spacy.matcher import Matcher
from spacy.language import Language

nlp = spacy.load("en_core_web_sm")
doc = nlp("Britain is a place. Mary is a doctor")

for ent in doc.ents:
    print(ent.text, ent.label_)

# removing GPE entities w custom component

@Language.component("remove_gpe")
def remove_gpe(doc):
    orignal_ents = list(doc.ents)
    for ent in doc.ents:
        if ent.label_ == "GPE":
            orignal_ents.remove(ent)
    doc.ents = orignal_ents
    print("hello")
    return doc

nlp.add_pipe("remove_gpe", after="ner")
# print(nlp.analyze_pipes())

doc = nlp("Britain is a place, Mary is a doctor")
for ent in doc.ents:
    print(ent.text, ent.label_)



