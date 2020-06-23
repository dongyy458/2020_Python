# !/usr/bin/python3
"""
  Author:  RuiJia. Cao
  Purpose: Generate random data set by iterator.
  Created: 16/6/2020
"""
import random
import string


def dataSampling(datatype, datarange, num, strlen=10):
    try:
        if num < 0:
            print("Please enter the correct number:")
        if strlen < 0:
            print("Please enter the correct string:")

        result = set()
        it = iter(datarange)
        if datatype is int:    # 整型
            while len(result) < num:
                item = random.randint(datarange[0], datarange[1])
                result.add(item)
                yield(item)

        elif datatype is float:    # 浮点型
            while len(result) < num:
                item = random.uniform(datarange[0], datarange[1])
                result.add(item)
                yield(item)

        elif datatype is str:    # 字符串型
            while len(result) < num:
                item = ''.join(random.SystemRandom().choice(datarange)
                               for _ in range(strlen))
                result.add(item)
                yield(item)
    except:
        raise


def dataScreening(data, *conditions):
    result = set()
    try:
        for i in data:
            if type(i) is int:
                it = iter(conditions)
                if next(it) <= i and next(it) >= i:
                    result.add(i)

            elif type(i) is float:
                it = iter(conditions)
                if next(it) <= i and next(it) >= i:
                    result.add(i)

            elif type(i) is str:
                for teststr in conditions:
                    if teststr in i:
                        result.add(i)
    except:
        print("No more!")

    return result


def apply():
    str_ex = string.ascii_letters + string.digits + string.punctuation
    # 整型
    result_1 = dataSampling(int, [0, 200], 00)
    print(dataScreening(result_1, 20, 60))
    # 浮点型
    result_2 = dataSampling(float, [0, 100], 100)
    print(dataScreening(result_2, 60, 70))
    # 字符串型
    result_3 = dataSampling(str, str_ex, 2000, 15)
    print(dataScreening(result_3, 'az', 'azzz'))


apply()