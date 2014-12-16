#Leon Oram
#16-12-2014
#Dev task 1

import random


def ask(select,caps,countr):
    country = countr[select]
    capital = caps[select]
    answ = input("The capital of {0} is ... ? ".format(country))
    answ = answ.title()
    if answ == capital:
        print("That is correct!")
    else:
        print("Incorrect! The capital is",capital)
    


def main():
    caps = ["Ottawa","London","Seoul","Tokyo","Pyongyang","Moscow","Washington","Vatican City","Kingston","Canberra"]
    countr = ["Canada","The United Kingdom","South Korea","Japan","Best Korea","Russia","The USA","Vatican City","Jamaica","Australia"]
    select = random.randint(1,10)
    ask(select,caps,countr)
    
    
user = input("Please enter your name: ")
user = user.lower()
if user != "kieran":
    main()
