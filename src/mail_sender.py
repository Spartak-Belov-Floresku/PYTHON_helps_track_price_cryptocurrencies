import smtplib


class SendAlert():
    def __init__(self, email, password, phone, text):
        self.__email = email
        self.__password = password
        self.__phone = phone
        self.__text = text
        self.__SendText()

    def __SendText(self):
        try:
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(self.__email, self.__password)

            subject = 'Crypto price alert'
            body = self.__text

            msg = 'Subject: {}\n\n{}'.format(subject, body)

            server.sendmail(
                    self.__email,
                    self.__phone,
                    msg,
                )

            server.quit()
            print("Email has been sent")
        except Exception as e:
            print("Email layer error -> "+str(e))

        
