# SpiritOrbs
## About
SpiritOrbs is an collection of different python functions I use on a regular basis.
## Documentation
### Random
As of now there are 2 random type functions.
#### Random_FL
Random_FL or Random From List is a function that accepts a list and returns a random item from it.<br />
Outputs same variable type as the item was in the list.
##### Syntax
    Random_FL(<List>)
##### Example
    List1 = [1, 2, 4]
    print(Random_FL(List1))
    Output:
    2
#### Random_Letters
Random_Letters is a function that takes random letters and makes a string out of them.
##### Syntax
    Random_Letters(<Number of lettors>, <Type True for numbers>)
##### Example
    print(Random_Letters(5, True))
    print(Random_Letters(6, False))
    Output:
    Hg6H8
    QbPyHV
### Print
As of now there is only 1 Print type function.
#### Print_NL
print_NL/print NewLine takes a list as an argument and prints each item in different lines.
##### Syntax
    print_NL(List)
##### Example
    List12 = [1, 5, "ab"]
    print_NL(List12)
    print_NL([1, "DC", 12, List12)
    Output:
    1
    5
    ab
    1
    DC
    12
    [1, 5, "ab"]
