import nltk


def download_nltk_data():
    nltk.download("punkt")
    nltk.download("stopwords")
    nltk.download("punkt_tab")


if __name__ == "__main__":
    download_nltk_data()
    print("NLTK data downloaded successfully.")
