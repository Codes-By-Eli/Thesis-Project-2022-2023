from bs4 import BeautifulSoup
import csv
import nltk
import pandas as pd
import lxml
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.stem.porter import PorterStemmer

from . import email_statistics
from constants import constants

def clean_html(html):
    soup = BeautifulSoup(html, features="lxml")
    texts = soup.get_text()
    text = word_tokenize(texts)
    return text

def remove_punctuations(words):
    words_no_punc = []

    for w in words:
        if w.isalpha():
            words_no_punc.append(w.lower())
    return words_no_punc

def remove_stopwords(words_no_punc):
    stopped = stopwords.words("english")
    clean_words = []
    for w in words_no_punc:
        if w not in stopped:
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
    return stats

def parse_email(email):
    no_tags_in_email = clean_html(email)
    no_punctuations = remove_punctuations(no_tags_in_email)
    no_stopwords = remove_stopwords(no_punctuations)
    stemmed_words = stemming_words(no_stopwords)
    email_statistics = perform_statistics(stemmed_words)
    return email_statistics

def create_email_stats(name_of_emails,contents_of_emails):
    print("Currently creating email stats....")
    all_email_stats = []
    #Create an entry object here with all the headers of the columns
    initial_entry = email_statistics.Statistics_Entry("File", "Access", "Account",
                                                      "Alert", "Click", "Confidential",
                                                      "Fradulent", "Indefinite", "Information",
                                                      "Notification", "Password", "Please",
                                                      "Provide", "Request", "Update",
                                                      "Upgrade", "Verify", "Result")
    all_email_stats.append(initial_entry)
    for i in range(len(contents_of_emails)):
        converted_content = contents_of_emails[i].lower()
        phishing = 1
        if "ham" in name_of_emails[i]:
            split_phrase = "date:"
            phishing = 0
        else:
            split_phrase = "x-keywords:"

        split_contents = converted_content.split(split_phrase)
        message_body = split_contents[1]
        email_stats = parse_email(message_body)
        email_stats.update({"Name": name_of_emails[i], "Phishing": phishing})

        #create stat_entry and append to all_email_stats
        entry = email_statistics.Statistics_Entry(email_stats["Name"], email_stats["access"], email_stats["account"], 
                                                  email_stats["alert"], email_stats["click"], email_stats["confidenti"],
                                                  email_stats["fradul"], email_stats["indefinit"], email_stats["inform"], 
                                                  email_stats["notif"], email_stats["password"], email_stats["pleas"], 
                                                  email_stats["provid"], email_stats["request"], email_stats["updat"], 
                                                  email_stats["upgrad"], email_stats["verif"], email_stats["Phishing"])
        all_email_stats.append(entry)
    return all_email_stats

def convert_to_csv(stats):
    with open(constants.CSV_PATH, "w") as stream:
        writer = csv.writer(stream)
        writer.writerows(stats)
    
    df = pd.read_csv(constants.CSV_PATH)
    print(df.head())