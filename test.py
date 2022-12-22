import numpy
import json
from functions.getData import readData, writeData
from functions.matrix import listToMatrix, uniformMatrix, multiplyMatrix, nullMatrix, einheitsMatrix, transponieren


def showMatrix(m):
    for x in m:
        print(x)

# with open('./words/nomen.txt', 'r', encoding='utf-8') as file:
#     x = file.read()

# y = x.split()

# # print(y)

# writeData('words/nomen.json', y)

# string = "Test Text für Strings und Chars"
# newList = list()

# for character in string:
#     newList.append(character)
#     print(character + ' is upper: ', character.isupper())

# print(newList)

# x = ['hallo']

# if type(x) == list:
#     print(x)


l1 = [1, 2, 3, 4]
m1 = uniformMatrix(listToMatrix(l1))
m2 = [
    [0, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 1, 1],
    [1, 1, 1, 1]
]
m3 = [
    [1, 0, 0, 0],
    [1],
    [1],
    [1]
]
m4 = [
    [0, 0, 0, 1],
    [0, 0, 1],
    [0, 1],
    [1]
]
showMatrix(uniformMatrix(m3))

print('-->')

showMatrix(multiplyMatrix(uniformMatrix(m3), einheitsMatrix(4)))
# showMatrix(multiplyMatrix(uniformMatrix(listToMatrix(l1)),
#            uniformMatrix(listToMatrix(l1))))
# showMatrix(transponieren(uniformMatrix(m3)))


# m1 = [[3, 2, 1], [1, 0, 2]]
# m2 = [[1, 2], [0, 1], [4, 0],]

# print(multiplyMatrix(m1, m2))
