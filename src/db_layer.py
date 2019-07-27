import urllib.request
import json
from decimal import Decimal, ROUND_HALF_UP

class ProcessData():
    def __init__(self, url, crypto, status, price):
        self.__json_obj = ""
        self.__url = url
        self.__crypto = crypto
        self.__user_asks_go = status
        self.__user_price = price
        self.__result = "N"
        self.__SendRequest()
        self.__ProccessCoinbaseData()
        
    #Here we are going to send request to Coinbase RESTFUL api and receive data in JSON format, it has default price for USD
    def __SendRequest(self):
        try:
            with urllib.request.urlopen(self.__url) as responce:
                self.__json_obj = json.loads(responce.read().decode("utf-8"))
                self.__json_obj = self.__json_obj['data']['rates']
        except Exception as e:
            self.__exceptionString("SendRequest", str(e))
            
    #Here JSON data is processed using user's parameters 
    def __ProccessCoinbaseData(self):
        try:
            for key in self.__json_obj:
                if key == self.__crypto:
                    coinbase_price_send_txt = (1/Decimal(self.__json_obj[key])).quantize(Decimal(".01"), rounding=ROUND_HALF_UP)
                    coinbase_price_check_users = (1/Decimal(self.__json_obj[key])).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
                    if self.__user_price < coinbase_price_check_users and self.__user_asks_go == "UP":
                        self.__result = "Price goes up "+str(coinbase_price_send_txt)
                    elif self.__user_price > coinbase_price_check_users and self.__user_asks_go == "DOWN":
                        self.__result = "Price goes down "+str(coinbase_price_send_txt)
        except Exception as e:
            self.__exceptionString("ProccessCoinbaseData", str(e))

    def __exceptionString(self, val, e):
        self.__result = "Error of data_base in "+val+" -> "+e


    def __str__(self):
        return self.__result
