#!bin/python3

from time import sleep
from climatics import *


temp = temperature.outside()
temp.updateWeaterData

coin = acceptor.coins()
credit = coin.getCredit()

while(True):
    tmpcredit = credit
    sleep(0.5)
    credit = coin.getCredit()

    if (tmpcredit != credit):
        print(credit)
        print(temp.toCelsius())


