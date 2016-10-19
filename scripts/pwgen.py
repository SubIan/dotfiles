import random

def genpw():
    pwout = ""
    list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"

    for x in range(0, 16):
        rand = random.random()
        char = list[int(rand * len(list))]
        pwout += char
    print(pwout)
count = int(input("How many passwords do you want?"))
for i in range(0, count):
    genpw()

