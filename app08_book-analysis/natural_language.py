import re
from pprint import pprint
import nltk
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer


with open("miracle_in_the_andes.txt") as file:
    book = file.read()
    
    
pattern = re.compile("[A-Za-z]+")
# transformo el book a minusculas para que poder comparar palabras
findings = re.findall(pattern, book.lower())
#print(findings)
#print(f"Size findings: {len(findings)}")

d = {}
for word in findings:
    if word in d:
        d[word] = d[word] + 1
    else:
        d[word] = 1
#print(d)

d_list = [(value, key) for key, value in d.items()]
d_list.sort(reverse=True)
#print(d_list[:10])

nltk.download('stopwords')
english_stopwords = stopwords.words("english")
#print(english_stopwords)

filtered_words = []
for count, word in d_list:
    if word not in english_stopwords:
        filtered_words.append((count, word))
pprint(filtered_words[:10])



#####################################################
# Sentiment Analysis:
#####################################################

# What is the most positivie and the most negative chapter?
#nltk.download('vader_lexicon')
analyzer = SentimentIntensityAnalyzer()
#print(type(analyzer))
#print(analyzer)
result = analyzer.polarity_scores("I love you")
print(result)
result = analyzer.polarity_scores("I hate you")
print(result)


pattern = re.compile("Chapter [0-9]+")
chapters = re.split(pattern, book)
chapters = chapters[1:]
for i, chapter in enumerate(chapters,1):
    result = analyzer.polarity_scores(chapter)
    print(f"Chapter {i}: {result}")
