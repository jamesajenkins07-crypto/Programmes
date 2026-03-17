#!/bin/python3

def strings(collection):
    count = 0

    for i in collection:
        if len(i) >= 3 and i[0] == i[-1]:
            count += 1

    return count

test = ['bgh', 'yuy', 'aa', 'wer', '1661']
print(strings(test))
