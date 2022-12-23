import numpy
import json
from functions.getData import readData, writeData
from functions.matrix import listToMatrix, uniformMatrix, multiplyMatrix, nullMatrix, einheitsMatrix, transponieren, enlargeMatrix
from functions.texttomatrix import strToList, strToMatrix, getStandardDevation


def showMatrix(m):
    for x in m:
        print(x)

# with open('./words/nomen.txt', 'r', encoding='utf-8') as file:
#     x = file.read()

# y = x.split()

# # print(y)

# writeData('words/nomen.json', y)


# ----->
# string = "Test Text für Strings, Chars und weiten Zeichen!"

# arr = string.split()

# y = list()
# for word in arr:
#     x = list()
#     for char in word:
#         print(charIndex(char))
#         x.append(char)
#     y.append(x)

# showMatrix(y)
# ----->

# newList = list()

# for character in string:
#     newList.append(character)
#     print(character + ' is upper: ', character.isupper())

# print(newList)

# x = ['hallo']

# if type(x) == list:
#     print(x)


# l1 = [1, 2, 3, 4]
# m1 = uniformMatrix(listToMatrix(l1))
# m2 = [
#     [0, 0, 0, 1],
#     [0, 0, 1, 1],
#     [0, 1, 1, 1],
#     [1, 1, 1, 1]
# ]
# m3 = [
#     [1, 0, 0, 0],
#     [1],
#     [1],
#     [1]
# ]
# m4 = [
#     [0, 0, 0, 1],
#     [0, 0, 1],
#     [0, 1],
#     [1]
# ]
# showMatrix(uniformMatrix(m3))

# print('-->')

# showMatrix(multiplyMatrix(uniformMatrix(m3), einheitsMatrix(4)))
# showMatrix(multiplyMatrix(uniformMatrix(listToMatrix(l1)),
#            uniformMatrix(listToMatrix(l1))))
# showMatrix(transponieren(uniformMatrix(m3)))


# m1 = [[3, 2, 1], [1, 0, 2]]
# m2 = [[1, 2], [0, 1], [4, 0],]

# print(multiplyMatrix(m1, m2))

# showMatrix(nullMatrix(2, 3))

# m1 = [
#     [1, 1, 1],
#     [2, 2, 2],
#     [3, 3, 3]
# ]

# showMatrix(transponieren(enlargeMatrix(m1, 3, 1)))

# char = 'ü'
# print(ord(char))

# hex = 97
# print(chr(hex))

# x = 0
# while x >= 0:
#     z = x
#     print('hex : ', z)
#     print('char: ', chr(z))
#     print('--------------')
#     x += 1

# print(charIndex('f'))

# m1 = strToMatrix('hallo! das ist mein name "Luis". Aber was vielleicht noch viel spannender ist, ist die Frage ob ich alles richtig schreibe. Denn ich reihenfolge spielt auch eine rolle')

m2 = strToMatrix(readData('words/nomen.json'))

# showMatrix(m2)

std = getStandardDevation(transponieren(m2))

x = getStandardDevation(transponieren(strToMatrix('Zuhause')))

print(x)
