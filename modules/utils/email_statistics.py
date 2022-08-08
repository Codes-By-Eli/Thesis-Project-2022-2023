class Statistics_Entry:
    def __init__(self, file_name, access_number, account_number, alert_number, 
                click_number, confidential_number, fradulent_number, 
                indefinite_number, information_number, notification_number, 
                password_number, please_number, provide_number, 
                request_number, update_number, upgrade_number, 
                verb_percentage, verify_number, phish_result):
        self.file_name = file_name
        self.access_number = access_number
        self.account_number = account_number
        self.alert_number = alert_number
        self.click_number = click_number
        self.confidential_number = confidential_number
        self.fradulent_number = fradulent_number
        self.indefinite_number = indefinite_number
        self.information_number = information_number
        self.notification_number = notification_number
        self.password_number = password_number
        self.please_number = please_number
        self.provide_number = provide_number
        self.request_number = request_number
        self.update_number = update_number
        self.upgrade_number = upgrade_number
        self.verb_percentage = verb_percentage
        self.verify_number = verify_number
        self.phish_result = phish_result

    def __str__(self):
        return f"""Name: {self.file_name}
                   Access: {self.access_number}
                   Account: {self.account_number}
                   Alert: {self.alert_number}
                   Click: {self.click_number} 
                   Confidential: {self.confidential_number}
                   Fradulent: {self.fradulent_number} 
                   Indefinite: {self.indefinite_number} 
                   Information: {self.information_number}
                   Notification: {self.notification_number} 
                   Password: {self.password_number} 
                   Please: {self.please_number}
                   Provide: {self.provide_number} 
                   Request: {self.request_number} 
                   Update: {self.update_number}
                   Verb: {self.verb_percentage}
                   Verify: {self.verify_number} 
                   Phishing {self.phish_result}"""

    def __iter__(self):
        return iter([self.file_name, self.access_number, self.account_number,
                     self.alert_number, self.click_number, self.confidential_number,
                     self.fradulent_number, self.indefinite_number, self.information_number,
                     self.notification_number, self.password_number, self.please_number,
                     self.provide_number, self.request_number, self.update_number,
                     self.upgrade_number, self.verb_percentage, self.verify_number, 
                    self.phish_result])