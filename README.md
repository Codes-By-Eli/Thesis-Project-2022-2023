# Title: Identification of Phishing Emails through Dataset Creation and Machine Learning

## Motivation Behind Research
* During my research into topics, there were many studies conducted on phishing websites with machine learning to determine phishing websites but not many did analysis into the contents of actual phishing emails to determine validity.
## Raw Data
* Phishing Emails
    * Taken from the phishing corpus
* Ham Emails
    * Originally .txt files that were converted into .eml files

## Data Processing
* Python Libraries Utilized
    * BeautifulSoup
    * csv
    * email
    * nltk
    * os
    * time
* Procedures
    1. The emails are parsed from the directory and converted into strings.
    2. Each email is cleaned of the html tags within its contents in order to just parse text.
    3. Each email is parsed for the contents found within ***Features Parsed From Emails*** through the following methods:
        * Using ntlk stemming feature to combine words that are the same inherently
        * Using nltk POS analysis to determine the amount of POS in an email
    4. Converting all of those emails into a .csv for data analysis.

## Features Parsed From Emails

1. Key Words (Stemmed)
    * Access
    * Account
    * Alert
    * Click
    * Confidential
    * Fradulent
    * Indefinite
    * Information
    * Notification
    * Password
    * Please
    * Provide
    * Request
    * Update
    * Upgrade
    * Verify
2. Percentage of POS in Emails
    * Verb Percentage

## Machine Learning Techniques

1. Decision Trees
2. K-Nearest Neighbors
3. Support Vector Machines
4. Linear Regression Analysis

## Results

| Analysis Technique | Accuracy (%) |
| :----------------: | :------: |
| Decision Tree      | 93.5     |
| KNN (Split)        | 93.5     |
| KNN (Cross-Val)    | 92.0     |
| SVM                | 90.5     |
| Linear Regression  | 90.6     |

## Obstacles

* Some of the phishing emails were too malicious to allow for analysis so they were removed from the dataset for safety concerns.
* The ham emails were orginally .txt files so they had to be converted into .eml files for consistency


## Important Documentation

* <a href="https://dl.acm.org/doi/10.1145/3419394.3423617">Who gets targeted by phishing emails?</a>
* <a href="https://cybersecurity.springeropen.com/articles/10.1186/s42400-019-0038-7">Survey of Intrusion Detection Systems</a>

