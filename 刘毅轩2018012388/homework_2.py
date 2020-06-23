# !/usr/bin/python3
"""
  Author:  YixuanLiu
  Purpose: Generate random data set.
  Created: 28/5/2020
"""
import random
import string


def generate(fun):
    def wrap(datatype, datarange, amount, *args, strlen=8):
        '''
        :Description:Generate a given Rangeition random data set.
        :param datatype: the data type you want to sample including int, float,str.
        :param datarange: iterable data set
        :param amount: the amount of random data you need
        :param strlen: delault length 8
        :return: a data set
        '''
        if amount < 0:
            print("Please input correct amount in generate.")
        if strlen < 0:
            print("Please input correct strlen in generate")
        result = set()
        if datatype == 'int':
            while len(result) < amount:
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                result.add(item)
        elif datatype == 'float':
            while len(result) < amount:
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                result.add(item)
        elif datatype == 'str':
            while len(result) < amount:
                item = ''.join(random.SystemRandom().choice(datarange)
                                for _ in range(strlen))
                result.add(item)
        print(result)
        return fun(result,*args)
    return wrap

@generate
def screen(data, dataType, *args):
    '''
        :Description: sampling data
        :param datatype: The type of data which include int, float and string
        :param data:iterable data set
        :return: a dataset
    '''
    s_result = set()
    for i in data:
        if (dataType == 'int'):
            Range = iter(args)
            if(next(Range) <= i <= next(Range)):
                s_result.add(i)
        elif (dataType == 'float'):
            Range = iter(args)
            if(next(Range) <= i <= next(Range)):
                s_result.add(i)
        elif (dataType == 'str'):
            for target in args:
                if(target in i):
                    s_result.add(i)
    print(s_result)


def apply():
    try:
        dataType = input('Enter your data type:   ')
        dataAmount = input('Enter the amount of data you want to generate:   ')
        dataAmount = int(dataAmount)
        if(dataType == 'str'):
            dataRange = input('Enter the rangr of data:')
        else:
            dataRangeTop = input('Enter the maximum of data you prefer:   ')
            dataRangeTop = int(dataRangeTop)
            dataRangeBottom = input('Enter the minimum of data you prefer:   ')
            dataRangeBottom = int(dataRangeBottom)
            dataRange = list()
            dataRange.append(dataRangeBottom)
            dataRange.append(dataRangeTop)
        if(dataType == 'str'):
            dataRange_2 = input('Enter data screening range:   ')
            s_result = screen(dataType,dataRange,dataAmount, dataType, dataRange_2)
        else:
            dataRangeBottom_2 = input(
                'Enter the minimum of data screening range:   ')
            dataRangeBottom_2 = int(dataRangeBottom_2)
            dataRangeTop_2 = input('Enter the maximum of data screening range:   ')
            dataRangeTop_2 = int(dataRangeTop_2)
            s_result = screen(dataType,dataRange,dataAmount, dataType, dataRangeBottom_2, dataRangeTop_2)
    except Exception as e:
        print(e)


apply()
