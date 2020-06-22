'''
Description:
本次作业内容：
1. 使用两个函数分别封装随机数生成和数据筛选功能。
2. 随机数生成函数至少支持整型、浮点型和字符串类型，数据类型、数据范围和数据个数等信息以输入参数方式传入函数。实现过程要求先判断数据类型再完成相应随机数生成，采用异常处理机制保证代码健壮性。
3. 数据筛选函数至少支持整型、浮点型和字符串类型，待筛选数据和筛选条件均作为参数传入，采用异常处理机制保证代码健壮性。
4. 调用上述封装函数进行测试，包括各种类型的随机数生成，然后给出多种条件进行筛选

Author：yuye.Dong
purpose:Generate random data set
Created:15/5/2020

'''
import random
import string

#数据生成
def rangedata_creat(dtype, drange, dnum):
    '''
    :Description: Generate a given condition random data list.
    :param dtype: the datatype you want to sample including int, float, string.
    :param drange: iterable data list
    :param dnum: the number of data you need
    :return: a data list
    '''
    chars = string.ascii_letters + string.digits

    try:
        if dnum < 0:
            print("Please input correct num .")

        L = []
        if dtype is int:

            L = [random.randint(0, drange) for _ in range(dnum)]



        elif dtype is float:
            L = [random.uniform(0, drange) for _ in range(dnum)]


        elif dtype is string:
            L = [''.join(random.sample(chars, 10)) for _ in range(dnum)]  # 列表转字符串




    except ValueError:
        print(" num error.")
    except NameError:
        print(" datatype Error.")
    except TypeError:
        print(" datatype Error.")
    except MemoryError:
        print("Maybe memory is full.")
    except:
        raise
    else:
        return L
    finally:
        print('end')


#数据筛选
def data_select(dtype, S):
    '''
        :Description: select out the right data in S
        :param dtype: the datatype you want to sample including int, float, string.
        :param S: the data list you have generated.
        :return: null
        '''
    selest2 = []

    try:
        for x in S:
            if dtype is int:
                if x >= 67 and x <= 100:
                    selest2.append(x)

            elif dtype is float:
                if x >= 20.0 and x <= 100.0:
                    selest2.append(x)

            elif dtype is string:
                if x.find('at'):
                    selest2.append(x)
        print(selest2)




    except Exception as e:
        print("default" + str(e))

#test
def apply():
    ''':Description:test.'''
    chars = string.ascii_letters + string.digits

    print('Test 1:')
    #test int
    S = rangedata_creat(int,100, 23)
    print(S)
    data_select(int, S)
    #test float
    print('Test 2:')
    S = rangedata_creat(float, 35, 20)
    print(S)
    data_select(float, S)
    #test string
    print('Test3:')
    S = rangedata_creat(string, chars, 20)
    print(S)
    data_select(string, S)





apply()