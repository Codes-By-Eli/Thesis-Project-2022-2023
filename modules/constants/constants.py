import os
HAM_PATH = './modules/emails/ham_emails'
HAM_FILES = os.listdir(HAM_PATH)

PHISHING_PATH = './modules/emails/phishing_emails'
PHISHING_FILES = os.listdir(PHISHING_PATH)

CSV_PATH = './modules/csv/ham_and_phish.csv'