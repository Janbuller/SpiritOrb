import random

# Print New Line
def print_NL(Printing = []):
    for i in Printing:
        print(i)

# Print List as String
def print_LAS(Printing = []):
    x = ""
    for i in Printing:
        x = x + i
    print(x)

# Random From List
def Random_FL(List = []):
    a = random.randint(0, len(List) - 1)
    return List[a]

# Random Letters
def Random_Letter(Amount = 1, Numbers = False, Letters_Used = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"):
    a = ""
    b = 0
    if Numbers == True:
        Letters_Used = Letters_Used + "12345678901234567890"
    while Amount > b:
        a = a + Letters_Used[random.randint(0, len(Letters_Used) - 1)]
        b += 1
    return a
