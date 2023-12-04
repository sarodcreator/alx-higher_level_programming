#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence != "":
        char = sentence[0]
    else:
        char = None
    return (len(sentence), char)
