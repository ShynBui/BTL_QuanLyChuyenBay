import math
from random import random

from saleapp import app


def cart_stats(list):
    total_price, total_quantity = 0, 0
    if list:
        for c in list.values():
            total_quantity += 1
            total_price += c['price']

    return {
        'total_price': total_price,
        'total_quantity': total_quantity
    }

from random import random


def generateOTP():
    # Declare a string variable
    # which stores all string
    string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    OTP = ""
    length = len(string)
    for i in range(6):
        OTP += string[math.floor(random() * length)]

    return OTP + ""


# if __name__ == '__main__':
#     with app.app_context():
#         print(generateOTP())