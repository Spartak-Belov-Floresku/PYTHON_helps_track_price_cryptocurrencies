#!/usr/bin/env python3
import time
from src.business_layer import GetData

def main():
    GetData(
        "https://api.coinbase.com/v2/exchange-rates",
        "ETH",# cryptocurrency that we want to track
        "DOWN",# if we want to track how price goes to DOWN or UP 
        222,# the price that we want
        'your_email_here@gmail.com',# Gmail that is used to send a text message
        'your_password_here', # password of email
        'your_phone_number_here@here_extension_of_your_provider',# phone number that is going to receive a notification
        # for example I use a ATT&T extension "@mms.att.net"
        )

if __name__=="__main__":
    while(True):
        main()
        time.sleep(60)# time interval to send a request and text message
