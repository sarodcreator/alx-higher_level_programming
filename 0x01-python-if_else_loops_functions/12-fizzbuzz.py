#!/usr/bin/python3
def fizzbuzz():
    i = 1
    for number in range(i, 101):
        if number % 3 == 0:
            print("Fizz", end=" ")
        elif number % 5 == 0:
            print("Buzz", end=" ")
        else:
            print("{}".format(number), end=" ")
