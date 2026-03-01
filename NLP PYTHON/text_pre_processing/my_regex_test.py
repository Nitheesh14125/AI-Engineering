import re 
#searching using regex
result_search = re.search("pattern",r"string to contain the pattern")
print(result_search)

result_search_2 = re.search("pattern",r"the pharse to find isn't in this string")
print(result_search_2)

#replacing old text with new text 

data = r"In our class Nithesh is a Brilliant and intelligent student"
replacement = re.sub("Nithesh","Nitheesh",data)
print(replacement)


#Finding the pattern and replacing 
customer_review = ["gagan was a great help to me in the store",
                   "the cashier was very rude to me , I think her name was vasanthi",
                   "amazing work from noor",
                   "Nitheesh was able to help me find the items I need quickly",
                   "Nithish was such a great addition to the team",
                   "Great service from Nithesh she found me what i wanted"]


#matching pattern with as part of word ? -> is to find remaining 
Nitheesh_reviews = []
pattern_to_find = r"Nith?"

for string in customer_review:
    if re.search(pattern_to_find,string):
        Nitheesh_reviews.append(string)
    
print(Nitheesh_reviews)

#matching pattern with letters starts with the a ^ -> is to find the starting 
pattern_to_find = r"^a"
a_reviews = []

for string in customer_review:
    if re.search(pattern_to_find,string):
        a_reviews.append(string)

print(a_reviews)

#matching pattern with ends with the y $ -> is to find ending 
pattern_to_find = r"y$"
y_reviews = []

for string in customer_review:
    if re.search(pattern_to_find,string):
        y_reviews.append(string)

print(y_reviews)


#matching pattern with ends with both like an or (want|need)ed -> | is used to find
need_Want_reviews = []
pattern_To_find = r"(need|want)ed"
for string in customer_review:
    if re.search(pattern_To_find,string):
        need_Want_reviews.append(string)

print(need_Want_reviews)


no_puntuation = []
pattern = r"[^\w\s]"
for string in customer_review:
    no_puntuation_string= re.sub(pattern," ",string)
    no_puntuation.append(no_puntuation_string)
print(no_puntuation)
