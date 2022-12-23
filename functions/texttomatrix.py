import numpy
from functions.getData import readData


def strToList(str):
    l = readData('letters/german_letters.json')
    newl = list()
    for x in l:
        newl.append(0)
    index = 0
    while index < len(l):
        for x in str:
            if x == l[index]:
                newl[index] = newl[index] + 1
        index += 1
    return newl


def strToMatrix(string):
    if type(string) == str:
        arr = string.split()
    elif type(string) == list:
        arr = string
    y = list()
    for word in arr:
        y.append(strToList(word))
    return y


def getStandardDevation(m):
    xmean = list()
    for x in m:
        xmean.append(numpy.mean(x))

    return xmean
