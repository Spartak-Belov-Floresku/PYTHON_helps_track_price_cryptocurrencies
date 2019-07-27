from src.db_layer import ProcessData
from src.mail_sender import SendAlert


class GetData():
    def __init__(self, url, crypto, status, price, email, password, phone):
        self.__url = url
        self.__crypto = crypto
        self.__status = status
        self.__price = price
        self.__email = email
        self.__password = password
        self.__phone = phone
        
        self.__ProcessData()


    def __ProcessData(self):
        result = str(ProcessData(self.__url, self.__crypto, self.__status, self.__price))
        if not result == "N":
            SendAlert(self.__email, self.__password, self.__phone, result)
            
