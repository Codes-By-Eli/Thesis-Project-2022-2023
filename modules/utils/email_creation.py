from colorama import Fore
import email
import os
import time

from ..constants import constants

def create_email_contents():
    print(Fore.YELLOW+ f"Currently creating email contents and names lists....")
    start = time.perf_counter()
    phishing_strings = []
    email_names = []
    for path in constants.PHISHING_FILES:
        phishing_email_directory = f"{constants.PHISHING_PATH}\\{path}"
        phishing_contents, phishing_names = parse_directory(phishing_email_directory)

        for i in range(len(phishing_contents)):
            phishing_strings.append(phishing_contents[i])
            email_names.append(phishing_names[i])
    
    for path in constants.HAM_FILES:
        ham_email_directory = f"{constants.HAM_PATH}\\{path}"
        ham_contents, ham_names = parse_directory(ham_email_directory)

        for i in range(len(ham_contents)):
            phishing_strings.append(ham_contents[i])
            email_names.append(ham_names[i])
    end = time.perf_counter()
    print(Fore.GREEN+ f"Success! Completed in: {end-start:0.4f} seconds")
    return email_names, phishing_strings

def parse_directory(dir):
    file_names = []
    texts = []
    folder_in_directory = os.listdir(dir)

    for fle in folder_in_directory:
        file_name = f"{dir}\\{fle}"       
        try:
            #print(f"Parsing file: {file_name}")
            msg = email.message_from_file(open(file_name))
            message = msg.as_string()
            texts.append(message)

            if "phishing" in file_name:
                file = file_name.split('phishing_emails\\')
            elif "ham" in file_name:
                file = file_name.split("ham_emails\\")
            file_names.append(file[1])
        except:
            print(f"Error on file: {file_name}")
           
    return texts, file_names

