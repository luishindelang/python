def uniformMatrix(m):
    lenth = 0
    for x in m:
        if lenth < len(x):
            lenth = len(x)
    for x in m:
        if len(x) < lenth:
            add = lenth - len(x)
            counter = 0
            while counter < add:
                x.append(0)
                counter += 1
    return m


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


def nullMatrix(ylenth, xlenth):
    my = list()
    y = 0
    while y < ylenth:
        x = 0
        mx = list()
        while x < xlenth:
            mx.append(0)
            x += 1
        my.append(mx)
        y += 1
    return my


def einheitsMatrix(ylenth, xlenth):
    m = nullMatrix(ylenth, xlenth)
    if ylenth >= xlenth:
        lenth = xlenth
    else:
        lenth = ylenth

    xy = 0
    while xy < lenth:
        m[xy][xy] = 1
        xy += 1

    return m


def enlargeMatrix(m, yadd, xadd):
    y = 0
    ylenth = len(m)
    while y < ylenth + yadd:
        if y < ylenth:
            x = 0
            while x < xadd:
                m[y].append(0)
                x += 1
        else:
            x = 0
            newlist = list()
            while x < ylenth + xadd:
                newlist.append(0)
                x += 1
            m.append(newlist)
        y += 1
    return m


def transponieren(m):
    m = uniformMatrix(m)
    ylenth = len(m)
    xlenth = len(m[0])
    my = list()
    x = 0
    while x < xlenth:
        y = 0
        mx = list()
        while y < ylenth:
            mx.append(m[y][x])
            y += 1
        my.append(mx)
        x += 1
    return my
