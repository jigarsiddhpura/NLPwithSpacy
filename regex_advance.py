import spacy
from spacy.tokens import Span
import re
from spacy.language import Language
from spacy.util import filter_spans

text = "Paul Newman was an American actor, but Paul Hollywood is a British TV Host. The name Paul is quite common."

pattern = r"Paul [A-Z]\w+"

matches = re.finditer(pattern, text)

for match in matches:
    print (match)

# doing above w spacy

nlp = spacy.blank('en')
doc = nlp(text)

original_ents = list(doc.ents)
# here original_ents is not getting print bcz its in a blank pipeline ⭐ 

mwt_ents = []
for match in re.finditer(pattern, doc.text):
    start , end  = match.span()
    span = doc.char_span(start,end)
    if span is not None:
        mwt_ents.append((span.start, span.end, span.text))

for ent in mwt_ents:
    start, end, name = ent
    per_ent = Span(doc, start, end ,'PERSON')
    original_ents.append(per_ent)
doc.ents = original_ents

for ent in doc.ents:
    print(ent.text, ent.label_)

print(mwt_ents)

# doing above thing using custom component

@Language.component("paul_ner")
def paul_ner(doc):
    pattern = r"Paul [A-Z]\w+"

    original_ents = list(doc.ents)
    # here original_ents is not getting print bcz its in a blank pipeline ⭐ 

    mwt_ents = []
    for match in re.finditer(pattern, doc.text):
        start , end  = match.span()
        span = doc.char_span(start,end)
        if span is not None:
            mwt_ents.append((span.start, span.end, span.text))

    for ent in mwt_ents:
        start, end, name = ent
        per_ent = Span(doc, start, end ,'PERSON')
        original_ents.append(per_ent)
    doc.ents = original_ents

    for ent in doc.ents:
        print(ent.text, ent.label_)

    return doc

nlp2 = spacy.blank("en")
nlp2.add_pipe("paul_ner")
doc2 = nlp2(text)
print(f'Ents using custom component : {doc2.ents}')

# Hollywood_ner

@Language.component("cinema_ner")
def cinema_ner(doc):
    pattern = r"Hollywood"

    original_ents = list(doc.ents)
    # here original_ents is not getting print bcz its in a blank pipeline ⭐ 

    mwt_ents = []
    for match in re.finditer(pattern, doc.text):
        start , end  = match.span()
        span = doc.char_span(start,end)
        if span is not None:
            mwt_ents.append((span.start, span.end, span.text))

    for ent in mwt_ents:
        start, end, name = ent
        per_ent = Span(doc, start, end ,'CINEMA')
        original_ents.append(per_ent)
    doc.ents = original_ents

    filtered = filter_spans(original_ents)

    for ent in doc.ents:
        print(ent.text, ent.label_)

    return doc

nlp3 = spacy.load("en_core_web_sm")
nlp3.add_pipe("cinema_ner")

print("-------------")
doc3 = nlp3(text)
for ent in doc.ents:
    print(ent.text, ent.label_)



