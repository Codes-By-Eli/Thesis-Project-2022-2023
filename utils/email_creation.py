import email
import os

def parse_directory(dir):
    file_names = []
    texts = []
    folder_in_directory = os.listdir(dir)

    for fle in folder_in_directory:
        file_name = f"{dir}\\{fle}"       
        try:
            msg = email.message_from_file(open(file_name))
            message = msg.as_string()
            texts.append(message)

            if "_phishing" in file_name:
                file = file_name.split('_phishing\\')
            elif "ham" in file_name:
                file = file_name.split("ham\\")
            file_names.append(file[1])
        except:
            print(dir + '\\'+ fle)
            print("Exception")
           
    return texts, file_names