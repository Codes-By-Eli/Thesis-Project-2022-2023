class Statistics_Entry:
    def __init__(self, file_name, access_number, account_number, alert_number, 
                click_number, confidential_number, fradulent_number, 
                indefinite_number, information_number, notification_number, 
                password_number, please_number, provide_number, 
                request_number, update_number, upgrade_number, 
                verify_number, phish_result):
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
        self.verify_number = verify_number
        self.phish_result = phish_result

    def __str__(self):
        return f"""Name: {self.file_name} \nAccess: {self.access_number} \nAccount: {self.account_number}\n
                   Alert: {self.alert_number} \nClick: {self.click_number} \nConfidential: {self.confidential_number}\n
                   Fradulent: {self.fradulent_number} \nIndefinite: {self.indefinite_number} \nInformation: {self.information_number}\n
                   Notification: {self.notification_number} \nPassword: {self.password_number} \nPlease: {self.please_number}\n
                   Provide: {self.provide_number} \nRequest: {self.request_number} \nUpdate: {self.update_number}\n
                   Verify: {self.verify_number} \nPhishing {self.phish_result}"""