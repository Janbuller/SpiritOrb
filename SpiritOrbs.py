#import random
from random import randint

# Print New Line
def print_NL(Printing: list):
    for i in Printing:
        print(i)

# Print List as String
def print_LAS(Printing: list):
    x = ""
    for i in Printing:
        x = str(x) + str(i)
    print(x)

# Random From List
def Random_FL(List: list):
    return List[randint(0, len(List) - 1)]

# Random Letters
def Random_Letters(Amount = 1, Numbers = False, Letters_Used = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"):
    a = ""
    b = 0
    if Numbers:
        Letters_Used = Letters_Used + "12345678901234567890"
    while Amount > b:
        a = a + Letters_Used[random.randint(0, len(Letters_Used) - 1)]
        b += 1
    return a
