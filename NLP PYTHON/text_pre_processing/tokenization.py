import nltk
nltk.download('punkt')

from nltk.tokenize import word_tokenize, sent_tokenize

sentences = "Her's cat name is Luna. Her's dog name is Bob"

# Sentence Tokenization
sente = sent_tokenize(sentences)
print("Sentences:", sente)

# Word Tokenization
words = word_tokenize(sentences)
print("Words:", words)