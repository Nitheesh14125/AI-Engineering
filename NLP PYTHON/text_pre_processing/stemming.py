from nltk.stem import PorterStemmer 
ps =PorterStemmer()

connect_tokens=["connecting","connectivity","connected","connects","connect","Inconnecting"]

for t in connect_tokens:
    print(t,":",ps.stem(t))

