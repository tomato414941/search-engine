import string

import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Download necessary NLTK data
nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)
nltk.download("punkt_tab", quiet=True)


class Preprocessor:
    def __init__(self):
        self.stemmer = PorterStemmer()
        self.stop_words = set(stopwords.words("english"))

    def preprocess(self, text):
        # Tokenization
        tokens = word_tokenize(text.lower())

        # Remove punctuation and non-alphabetic tokens
        tokens = [token for token in tokens if token.isalpha()]

        # Remove stop words and apply stemming
        tokens = [
            self.stemmer.stem(token) for token in tokens if token not in self.stop_words
        ]

        return tokens


preprocessor = Preprocessor()
