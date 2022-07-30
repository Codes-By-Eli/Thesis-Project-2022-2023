from bs4 import BeautifulSoup
import nltk
import lxml
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.stem.porter import PorterStemmer
import email_statistics

def clean_html(html):
    soup = BeautifulSoup(html)
    text = soup.get_text()
    return text

def remove_punctuations(words):
    words_no_punc = []

    for w in words:
        if w.isalpha():
            words_no_punc.append(w.lower())
    return words_no_punc

def remove_stopwords(words_no_punc):
    stopwords = stopwords.words("english")
    clean_words = []
    for w in words_no_punc:
        if w not in stopwords:
            clean_words.append(w)
    return(clean_words)

def stemming_words(clean_words):
    porter = PorterStemmer()
    stem_words = []
    for w in clean_words:
        stem_words.append(porter.stem(w))
    return(stem_words)

def perform_statistics(stemmed):
    stats = {}
    word_check = ["account", "inform", "updat", "pleas", "secur", "alert",
                  "request", "click", "fradul", "notif", "upgrad", "indefinit",
                  "access", "password", "verif", "provid", "confidenti"]
    for el in word_check:
        stats.update({el: 0})
    for el in stemmed:
        if el in word_check:
            stats[el] += 1

def parse_email(email):
    no_tags_in_email = clean_html(email)
    no_punctuations = remove_punctuations(no_tags_in_email)
    no_stopwords = remove_stopwords(no_punctuations)
    stemmed_words = stemming_words(no_stopwords)
    email_statistics = perform_statistics(stemmed_words)