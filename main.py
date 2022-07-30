import email
from constants import constants
from utils import email_creation


def main():
    phishing_files = ['20051114',  'phishing0', 'phishing2', 'phishing3']
    phishing_strings = []
    email_names = []
    for path in phishing_files:
        phishing_email_directory = f"{constants.PHISHING_PATH}\\{path}"
        phishing_contents, phishing_names = email_creation.parse_directory(phishing_email_directory)

        for i in range(len(phishing_contents)):
            phishing_strings.append(phishing_contents[i])
            email_names.append(phishing_names[i])
    
    ham_contents, ham_names = email_creation.parse_directory(constants.HAM_PATH)

    for name in ham_names:
        email_names.append(name)

    print(len(email_names))

main()
