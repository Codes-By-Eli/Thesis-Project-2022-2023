from colorama import Fore
import time

from constants import constants
from utils import csv_creator
from utils import email_creation



def create_email_contents():
    print(Fore.YELLOW+ f"Currently creating email contents and names lists....")
    start = time.perf_counter()
    phishing_strings = []
    email_names = []
    for path in constants.PHISHING_FILES:
        phishing_email_directory = f"{constants.PHISHING_PATH}\\{path}"
        phishing_contents, phishing_names = email_creation.parse_directory(phishing_email_directory)

        for i in range(len(phishing_contents)):
            phishing_strings.append(phishing_contents[i])
            email_names.append(phishing_names[i])
    
    ham_contents, ham_names = email_creation.parse_directory(constants.HAM_PATH)

    for i in range(len(ham_contents)):
        phishing_strings.append(ham_contents[i])
        email_names.append(ham_names[i])
    end = time.perf_counter()
    print(Fore.GREEN+ f"Success! Completed in: {end-start:0.4f} seconds")
    return email_names, phishing_strings

def main():
    email_names, phishing_strings = create_email_contents()
    all_stats = csv_creator.create_email_stats(email_names, phishing_strings)
    
    csv_creator.convert_to_csv(all_stats)

main()
