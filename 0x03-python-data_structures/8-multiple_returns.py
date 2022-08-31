#!/usr/bin/python3
def multiple_returns(sentence):
    a = int(len(sentence))

    if a == 0:
        return (a, None)

    b = str(sentence[0])
    return(a, b)
