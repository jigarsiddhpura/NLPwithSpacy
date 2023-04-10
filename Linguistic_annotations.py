import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

with open("data\wiki_us.txt",'r') as f:
    text = f.read()

# creating a doc OBJECT
doc = nlp(text)

# print(len(doc))
# print(len(text))

# for token in text[:10]:
#     print(token)
# for token in doc[:20]:
#     print(f'token = {token}, entity_type = {token.ent_type_}')
    

# doc.sents -> generator object
# for sent in doc.sents:
    # print(sent)

sent1 = list(doc.sents)[0]
print(f'sentence = {sent1}')
token2 = sent1[2]

print(token2)
# print(token2.text)

# left & right edge of a span
print(token2.left_edge)
print(token2.right_edge)

# entity types
print(token2.ent_type)
print(token2.ent_type_)
# GPE - GEOPOLITICAL ENTITY IN NER
print(token2.ent_iob_)
# I -> Inside a large entity, B -> @ Beggining of entity, O -> Outside a entity

print(f'lemma of {sent1[11]} = {sent1[11].lemma_}')
print(f'lemma of {sent1[12]} = {sent1[12].lemma_}')

# morphs
print(f'morph of token2 -> {token2.morph}')
print(sent1[12].morph)

# part of speech
print(token2.pos_)

# dependency relation
print(token2.dep_)

print(token2.lang_)

sample = "Jigar enjoys travelling different places!"
doc2 = nlp(sample)
for token in doc2:
    print(token.text, token.pos_, token.dep_)

# displacy.render(doc2, style='dep')
# above line use if in collab n below for vscode

html = displacy.render(doc2, style="dep", options={"compact": True, "color": "blue"})
with open("outputDisplacy.html", "w", encoding="utf-8") as file:
    file.write(html)
