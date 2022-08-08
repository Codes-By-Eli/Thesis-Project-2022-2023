from modules.constants import ascii_art
from modules.utils import csv_creator, email_creation

def main():
    print(ascii_art.create_initial_art())
    email_names, phishing_strings = email_creation.create_email_contents()
    all_stats = csv_creator.create_email_stats(email_names, phishing_strings)
    
    csv_creator.convert_to_csv(all_stats)

main()
