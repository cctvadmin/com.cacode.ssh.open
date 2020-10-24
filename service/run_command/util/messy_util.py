def toBigWrite(string):
    """
    转大写
    :param string:
    :return:
    """
    result = []
    for i in string:
        result.append(str(i).upper())
    return result


def toSmWrite(string):
    """
    全部转小写
    :param string:
    :return:
    """
    result = []
    for i in string:
        result.append(str(i).lower())
    return result


def notNull(string):
    return not string is None and not string == ''


def allNotNull(string=None):
    """
    所有参数不为空
    :param string:
    :return:
    """
    for i, j in enumerate(string):
        if not notNull(j):
            return i, False
    return -1, True


if __name__ == '__main__':
    # print(toBigWrite(['afaasdahsid', 'ashdkha']))
    # print(toSmWrite(['afaasdahsid', 'SADFHAIJDSHFUIA']))
    pass
