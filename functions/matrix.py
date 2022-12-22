def multiplyMatrix(m1, m2):
    m1x = len(m1[0])
    m1y = len(m1)
    m2x = len(m2[0])
    my = list()
    y1 = 0
    while y1 < m1y:
        mx = list()
        x2 = 0
        while x2 < m2x:
            x1 = 0
            z = 0
            while x1 < m1x:
                z += m1[y1][x1] * m2[x1][x2]
                x1 += 1
            mx.append(z)
            x2 += 1
        my.append(mx)
        y1 += 1
    return my


def uniformMatrix(m):
    maxLenth = 0
    for x in m:
        if maxLenth < len(x):
            maxLenth = len(x)
    for x in m:
        if len(x) < maxLenth:
            add = maxLenth - len(x)
            counter = 0
            while counter < add:
                x.append(0)
                counter += 1
    return m


def listToMatrix(l):
    my = list()
    lenth = len(l)
    y = 0

    while y < lenth:
        x = y
        mx = list()
        while x < lenth:
            mx.append(l[x])
            x += 1
        my.append(mx)
        y += 1
    return my


def nullMatrix(lenth):
    my = list()
    y = 0
    while y < lenth:
        x = 0
        mx = list()
        while x < lenth:
            mx.append(0)
            x += 1
        my.append(mx)
        y += 1
    return my


def einheitsMatrix(lenth):
    m = nullMatrix(lenth)
    xy = 0
    while xy < lenth:
        m[xy][xy] = 1
        xy += 1

    return m


def transponieren(m):
    lenth = len(m)
    my = list()
    x = 0
    while x < lenth:
        y = 0
        mx = list()
        while y < lenth:
            mx.append(m[y][x])
            y += 1
        my.append(mx)
        x += 1
    return my
