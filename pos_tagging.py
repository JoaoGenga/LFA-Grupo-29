import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords

def process_text(text):
    tokens = word_tokenize(text)
    sWords = set(stopwords.words('english'))
    cleanTokens = [w for w in tokens if not w in sWords]
    tagged = nltk.pos_tag(cleanTokens)
    tags_only = [tag for _, tag in tagged]
    return tags_only

sentence = "What time is it"
print(process_text(sentence))
