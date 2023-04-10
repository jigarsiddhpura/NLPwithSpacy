import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

with open("data\wiki_us.txt",'r') as f:
    text = f.read()

# creating a doc OBJECT
doc = nlp(text)

for ent in doc.ents:
    print(ent.text, ent.label_)

# displacy.render(doc, style='ent')

html = displacy.render(doc, style="ent", options={"compact": True, "color": "blue"})
with open("EntDisplacy.html", "w", encoding="utf-8") as file:
    file.write(html)

