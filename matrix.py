def multiplyMatrix(m1, m2):
    result = list()

    m1x = len(m1[0])
    m1y = len(m1)
    m2x = len(m2[0])

    x2 = 0
    while x2 < m2x:
        r = list()
        y1 = 0
        while y1 < m1y:
            x1 = 0
            z = 0
            while x1 < m1x:
                z += m1[y1][x1] * m2[x1][x2]
                x1 += 1
            r.append(z)
            y1 += 1
        result.append(r)
        x2 += 1
    return result


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
