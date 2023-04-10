import spacy
from spacy import displacy
import numpy as np

# md - medium , includes word vectors
nlp = spacy.load("en_core_web_md")

with open("data\wiki_us.txt",'r') as f:
    text = f.read()

# creating a doc OBJECT
doc = nlp(text)
sent1 = list(doc.sents)[0]

#  ❌❌❌❌❌❌❌❌❌❌❌

# my_word = "country"

# ms = nlp.vocab.vectors.most_similar(
#     np.asarray([nlp.vocab.vectors[nlp.vocab.strings[my_word]]]), n=10)
# words = [nlp.vocab.strings[w] for w in ms[0][0]]
# distances = ms[2]
# print(words)

#  ❌❌❌❌❌❌❌❌❌❌❌

word1 = nlp("country")
vector1 = word1.vector
print(vector1.shape)

# Find similar words to "country"
similar_words = []
for word in nlp.vocab:
    if word.has_vector and word.is_lower and word.is_alpha:
        similarity = word1.similarity(word)
        # similarity depends on semantic meaning of words
        if similarity > 0.5:
            similar_words.append((word.text, similarity))

# Sort the similar words by similarity score
similar_words = sorted(similar_words, key=lambda x: -x[1])

# Print the top 10 most similar words
for word in similar_words[:10]:
    print(word[0])

doc1 = nlp("Jigar loves travelling")
doc2 = nlp("Mahek loves watching netflix")
print(doc1.similarity(doc2))
