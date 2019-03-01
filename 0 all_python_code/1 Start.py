#!/usr/bin/env python
# coding: utf-8
# by Tianbiao Yang
# Time: 2018-11-12

print("Hello,world!")

b = [1, 2, 3]

# get_ipython().run_line_magic('pinfo', 'b')

# get_ipython().run_line_magic('pinfo', 'print')

def add_numbers(a, b):
    """
    Add two numbers together
    Returns
    -------
    the_sum : type of arguments
    """
    return a + b

get_ipython().run_line_magic('pinfo', 'add_numbers')
get_ipython().run_line_magic('pinfo2', 'add_numbers')
get_ipython().run_line_magic('psearch', 'np.*load*')

import numpy as np
get_ipython().run_line_magic('psearch', 'np.*load*')

# %load 1 ipython_script_test.py
def add_numbers(a, b):
    """
    Add two numbers together
    Returns
    -------
    the_sum : type of arguments
    """
    return a + b


# %load 1_ipython_script_test.py
def f(x, y, z):
	return (x + y) / z
a = 5 
b = 6
c = 7.5
result = f(a, b, c)

get_ipython().run_line_magic('run', '1_ipython_script_test.py')

a = np.random.randn(100,100)


# 检查代码执行时间
get_ipython().run_line_magic('timeit', 'np.dot(a, a)')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt
plt.plot(np.random.randn(50).cumsum())

a =[1, 2, 3]

b = a
a.append(4)
def append_element(some_list, element):
    some_list.append(element)

data = [1, 2, 3]
append_element(data, 6)
a = 2; b = 3.4
isinstance(a, (int, float))
isinstance(data, (int, float))


# 鸭子类型：看起来像鸭子，叫起来像鸭子，我们就说是鸭子
# 例如验证实现迭代器协议，它一定可以迭代
def isiterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:#不可遍历
        return False

isiterable([2])

# check the data type 检查对象是不是一个列表或者NumPy数组
if not isinstance(a, list) and isiterable(a):
    a = list(a)
    # a = np.array(a)

a = (1, 2, 3)

# 二元运算符
a = 10
b = 5
a // b # a 整除以 b
a ** b # a 的 b次方
a & b # a 与 b
a | b # a 或 b
a ^ b # 对布尔值
a == b
a != b
a <= b
a >= b
# 两者为同一python对象
a is b 
a is not b

# python的字符串和元组是不可变的
# 可变对象和不可变对象
# 可变对象：数组，列表，字典
a_list = ['foo',2, [4,5]]
a_list[2] = (3, 4)

# 不可变对象：字符，元组
a_tuple = (1, 2, (3, 4))

a_tuple[1] = "four"


c = """
Hello,
the world!
"""
c.count('\n')


# 字符串格式化
# 函数format()
tem = '{0:.2f} {1:s} are worth Us${2:d}'
tem.format(4.55656, "Arefgbdhfu sa", 1)


# 类型转化
# str(), int(), float(), bool()
s = '3.141592653'
s_float = float(s)
type(s_float)
int(s_float)
bool(s_float)
bool(0)

# 时间datatime函数
from datetime import datetime, time, date
dt = datetime(2018, 11, 7, 10, 2, 1)
print(dt.day)
print(dt.date())
print(dt.time())
dt.date()

# strftime()将datatime转化成字符串
dt.strftime('%m/%d/%Y %H:%M:%S')

# strptime()将字符串转换成datatime对象
datetime.strptime('20181107','%Y%m%d')
# replace()替换
dt.replace(minute = 0, second = 0)
dt2 = datetime(2011, 2, 12, 11, 22, 12)
delta = dt - dt2
delta


dt2 + delta

x = int(input('请输入一个数字：'))
if x > 0:
    print('x > 0')
elif x == 0:
    print('x = 0')
else :
    print('x < 0')


a =[1, 2, 3, 4]
b = 2
for i in a:
    if i == 3:
        break
    b += i


# range()生成等差整数序列
range(10)
list(range(10))
list(range(0, 20, 2))
a = list(range(0, 20, 2))
for i in range(len(a)):
    val = a[i]
val
