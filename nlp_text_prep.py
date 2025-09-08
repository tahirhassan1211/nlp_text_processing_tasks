# In TextProcessing  we perform following task for text preprocessing and preparation
# 1. Incorrect Spelling Correction
# 2. Remove Punctuation
# 3. Convert to Lowercase
# 4. text splittin or tokenization
# 5. Remove Stop words


#import re
import nltk
#nltk.download('punkt_tab')
import string
string.punctuation
exclude = string.punctuation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
from textblob import TextBlob

text = "Hello there, howw are you doing today? The weeather is greaty, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."
print(text)

txtblob=TextBlob(text)
text=txtblob.correct().string
text1= word_tokenize(text)
text2= sent_tokenize(text)
print(text1)
print(text2)
def remove_punc(text):
    return text.translate(str.maketrans('', '',exclude))

text=remove_punc(text)
print(text)
#text = re.sub(r'[^\w\s]', '', text)
text = text.lower().split()
print(text)
print(len(text))

stop_words = set(stopwords.words('english'))
for word in text:
    if word in stop_words:
        text.remove(word)
print(text)
print(len(text))
text = ' '.join(text)
print(text)
