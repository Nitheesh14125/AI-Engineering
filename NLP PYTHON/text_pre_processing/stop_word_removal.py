import nltk 
from nltk.corpus import stopwords 
nltk.download('stopwords')


en_stopwords = stopwords.words('english')
print(en_stopwords)

sentence = "it was too far to go to the shop and he did not want her to walk"
words = sentence.split()

print("Before stop word removal = ",words)
filtered_words = []
for word in words:
    if word not in en_stopwords:
        filtered_words.append(word)

print("After stop word removal = ",filtered_words)