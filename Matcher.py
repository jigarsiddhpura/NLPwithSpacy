import spacy 
from spacy.matcher import Matcher
import json

nlp = spacy.load("en_core_web_sm")

matcher = Matcher(nlp.vocab)
pattern = [
    {"LIKE_EMAIL":True}
]
matcher.add("EMAIL_ADDRESS", [pattern])

doc = nlp("Thsi is email address : abc@winner.com")
matches = matcher(doc)
# print(matches)

# matches[0][0] is a lexeme
# print(f'Label = {nlp.vocab[matches[0][0]].text}')

with open ("data\wiki_mlk.txt", "r") as f:
    text = f.read()

#grabing all proper noun followed with verb
matcher2 = Matcher(nlp.vocab)
pattern2 = [
    {"POS":"PROPN", "OP":"+"}, {"POS":'VERB'}
    # {"IS_ALPHA": True}, {"IS_DIGIT": True, "OP": "+"}
]
matcher2.add("PROPER_NOUNS",[pattern2], greedy='LONGEST')
doc2 = nlp(text)
matches2 = matcher2(doc2)
# print(len(matches2))
matches2.sort(key=lambda x : x[1])
# for match in matches2[:10]:
#     print(match, doc2[match[1]:match[2]])



#grabbing speaker name who said the quote

with open("data/alice.json",'r') as f:
    # for json file replace \ -> / ⭐
    data = json.load(f)
text3 = data[0][2][0]
text3 = text3.replace("`","'")
print(text3)

speak_lemmas = ["think", "say", "tell"]

matcher3 = Matcher(nlp.vocab)
pattern3 = [
    {"ORTH":"'"},
    {"IS_ALPHA": True, "OP": "+"}, 
    {"IS_PUNCT":True, "OP": "*"},
    {"ORTH":"'"},
    {"POS":'VERB', "LEMMA":{'IN': speak_lemmas}},
    {"POS":"PROPN", "OP":"+"},
    {"ORTH":"'"},
    {"IS_ALPHA": True, "OP": "+"}, 
    {"IS_PUNCT":True, "OP": "*"},
    {"ORTH":"'"}
]
pattern4 = [{'ORTH': "'"},
 {'IS_ALPHA': True, "OP": "+"},
 {'IS_PUNCT': True, "OP": "*"}, {'ORTH': "'"},
  {"POS": "VERB", "LEMMA": {"IN": speak_lemmas}},
  {"POS": "PROPN", "OP": "+"}
  ]
pattern5 = [{"POS": "PROPN", "OP": "+"},
{"POS": "VERB", "LEMMA": {"IN": speak_lemmas}},
 {'ORTH': "'"}, {'IS_ALPHA': True, "OP": "+"},
 {'IS_PUNCT': True, "OP": "*"},
 {'ORTH': "'"}
 ]
matcher3.add("PROPER_NOUNS",[pattern3, pattern4, pattern5], greedy='LONGEST')
doc3 = nlp(text3)
matches3 = matcher3(doc3)
print(len(matches3))
matches3.sort(key=lambda x : x[1])
for match in matches3[:10]:
    print(match, doc3[match[1]:match[2]])