#!/usr/bin/env python
# coding: utf-8
# by Tianbiao Yang
# Time: 2018-11-12


## 元组
tup = 4, 5, 6

# tup 函数将任意序列或迭代器转变成元组
tuple([1, 2, 3])
tup = tuple("string")
tup[1].append(3)

# 元组拆包
tup = 4, 5, 6
a, b, c = tup


# 常用场景：遍历元组或列表里组成的序列, format():字符串的格式化
sep = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a, b, c in sep:
    print('a = {0}, b = {1}, c = {2}'.format(a, b, c))


# *...指剩余部分
value = 1, 2, 3, 4, 5, 6, 7
a, b, *rest = value
# data wished to lose，insteat of '*_'
a, b, *_ = value

# count():计算数目
a = (3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7)
a.count(4)


# list():常用来将迭代器或生成器转换成列表
a = list(range(10))

# append(): add the element
a.append("de")

# insert（）指定位置插入
a.insert(0, 'de')

# pop（）指定位置删除
a.pop(2)
a.remove('de')

# 连接有两个 ’+‘或者extend()
# 存在int类型不能迭代的情况
a = [0, 2, 3, 4, 5, 6, 7, 8, 9]
a_1 = []
for i in a:
    # print(i)
    a_1.extend(str(i))
a_1

# sort():sorting
a_1.sort()
a_1.sort(key =len)


# bisect():进行二分搜索和已排序列表维护
import bisect 
bisect.bisect(a, 10)
bisect.insort(a,-1)


# 切片
seq = list(range(10))
seq[3:4] = [0, 0]
seq[:5]
seq[3:]
seq[::2]
seq[::-1]


# enumerate()方法对数据建立索引，常用方式是建立一个字典，将序列值mapping到索引位置
mapping = {}
for i, value in enumerate(seq):
    mapping[i] = value


# 排序（正序）：sorted()方法和sort()类似，但前者会生成一个复制，而后者修改原数据
seq = [0, 1, 2, 0, 0, 4, 5, 6, 7, 8, 9]
print(seq)
print(sorted(seq))
seq.sort()
print(seq)


# 排序(倒序)：reversed()
seq = [0, 1, 2, 0, 0, 4, 5, 6, 7, 8, 9]
print(seq)
print(list(reversed(seq)))
print(list(reversed(sorted(seq))))


# zip()用于元素之间的配对
seq1 = ['dd','ss', 'dd']
seq2 = ['o', 'f','h']
zipped = list(zip(seq1,seq2))
# 常用场景：同时遍历多个序列，有时和enumerate连用
for i, (a,b) in enumerate(zip(seq1,seq2)):
    print('{0}: {1}, {2}'.format(i, a, b))
# 可在再拆回来
seq1_1, seq2_1 = zip(*zipped)


# 字典
empty_dict = {}
d1 = {'a' : 'some value', 'b' : [1, 2, 3, 4]}

# 删除：del(), pop()
# del()
d1 = {'a': 'some value', 'b': [1, 2, 3, 4], 'w': 1}
del d1['w']
d1
# pop()
d1 = {'a': 'some value', 'b': [1, 2, 3, 4], 'w': 1}
d1['w'] = 1
ret = d1.pop('b')

# 将d1的key以列表输出
list(d1.keys())

# update()
# 合并字典 
d1.update({'d': 1})
d1


mapping = dict(zip(range(5),range(5)))
mapping

seq1 = ['dd','ss', 'dd']
seq2 = list(range(3))
mapping = {}
for key, value in zip(seq2, seq1):
    mapping[key] = value
mapping



some_dict = mapping
print(some_dict)
value = []
if key in some_dict:
    value = value.append(some_dict[key])
else:
    value = default_value
print(value)


default_value = '1'
value = some_dict.get(key,default_value)
value


words = ['apple', 'bat', 'bar', 'attom', 'book']
by_letter_v0 = {}
for word in words:
    letter = word[0]
    if letter not in by_letter_v0:
        by_letter_v0[letter] = [word]
    else:
        by_letter_v0[letter].append(word)
print(by_letter_v0)

# setdefault()
by_letter_v1 = {}
for word in words:
    letter = word[0]
    by_letter_v1.setdefault(letter, []).append(word)
print(by_letter_v1)

# defaultdict()
# 生成符合要求的字典，在字典的各位置传入类型或在各位置生成默认值
from collections import defaultdict
by_letter = defaultdict(list)
for word in words:
    by_letter[word[0]].append(word)
print(by_letter)
print(list(by_letter))


# hush()： 检验对象是否可以哈希化（用作字典的键）
hash('string')


# hash((1, 2, [3, 4])) # TypeError
# 解决方法，将list转化成元组，只要元组的元素可以哈希化，则元组可以哈希化
print(1, 2, tuple([3, 4]))
hash((1, 2, tuple([3, 4])))


## 集合
# set()
# 创建集合
set([2, 2, 2, 1, 1, 3, ])

# 集合的常规操作
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7, 8}
# 并集
print(a.union(b), a | b)
# 交集
print(a.intersection(b), a & b)
# 将a设置成b的并集和交集
a.update(b)
print(a)
# add element
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7, 8}
a.add(6)
print(a)
# clear set or remove element 
# a.clear()
a.remove(6)
print(a)
# 随机删除
a.pop()
# 在a不在b
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7, 8}
print(a.difference(b), a - b)
a.difference_update(b)
print(a)
# 交集的补集
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7, 8}
print(a.symmetric_difference(b))
a.symmetric_difference_update(b)
print(a)
# a包含于b返回True 
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7, 8}
a.intersection_update(b)
a.issubset(b)
# a包含b返回True 
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7, 8}
a.update(b)
a.issuperset(b)
# a与b没交集返回True
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7, 8}
a.difference_update(b)
a.isdisjoint(b)


# ** 对于大型数据集，这样更高效
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7, 8}
c = a.copy() 
c | b

## 列表，集合和字典的推导式
'''
列表基本形式：[expr for val in collection in condition]
等价于下面的形式
result = []
for val in collection:
    if condition:
        result.append(expr)
'''
words = ['apple', 'bat', 'bar', 'attom', 'book']
# upper小写转化成大写
[x.upper() for x in words if len(x) > 3]

# 字典基本形式： dict_comp = {key_expr : value_expr for value in collection if condition}
# 集合基本形式：set_comp = {expr for value in collection if condition}
words = ['apple', 'bat', 'bar', 'attom', 'book']
unique_lengths = {len(x) for x in words}
print(unique_lengths)
# mapping简洁的表达形式
set(map(len, words))


words = ['apple', 'bat', 'bar', 'attom', 'book']
loc_mapping = {index: val for index, val in enumerate(words)}
loc_mapping


words = [['apple', 'bat', 'bar'], ['attom', 'book']]
word_of_interest = []
for word_group in words:
    each_words = [word for word in word_group if word.count('o') >= 2]
    word_of_interest.extend(each_words)
word_of_interest

# 推导式
result = [word for word in each_words for each_words in words if word.count('o') >= 2]
result

## 函数
def func():
    a = []
    for i in range(5):
        a.append(i)
    return a
func()

def bind_a_variable():
    global a
    a = []
    return a
bind_a_variable()

def func():
    for i in range(5):
        a.append(i)
    return a, 2*a
func()


# 函数是对象，下例为数据清洗
states = ['  Alll ', 'gg!', 'gg', 'GG', 'DoooLuu', 'south    daelll##', 'west ll?']
# 正则表达式模块 re，需要重点学习
import re
def clean_strings(states):
    result = []
    for value in states:
        value = value.strip( )
        value = re.sub('[!#?]', ' ', value)
        value = value.title()
        result.append(value)
    return result
clean_strings(states)

def rm_punctuation(value):
    return re.sub('[!#?]', ' ', value)
clean_ops = [str.strip, rm_punctuation, str.title]

def clean_strings(strings, ops):
    result = []
    for value in strings:
        for func in ops:
            value = func(value)
        result.append(value)
    return result
clean_strings(states, clean_ops)

for x in map(rm_punctuation, states):
    print(x)

# 匿名(Lambda)函数
def short_function(x):
    return x * 2
short_function(2)
# 与下式等价
equiv_anon = lambda x: x * 2
equiv_anon(3)


# 柯里化
def add_numbers(x, y):
    return x + y
add_five = lambda y: add_numbers(5, y)

# 生成器
def squares(n = 10):
    print('data from 1 to {0}'.format(n **2))
    for i in range(1, n + 1):
        yield i ** 2
gen = squares()
# 只有在请求生成器的元素时，它才会执行
for i in gen:
    print(i,end = ' ')


# 生成器表达式
gen = (x ** 2 for x in range(100))
# 有时可代替推导式
sum(x ** 2 for x in range(100))
dict((i, i ** 2) for i in range(5))


# itertools模块
import itertools
words = ['apple', 'bat', 'bar', 'attom', 'book']
first_words = lambda x: (x[0])
for letter, words in itertools.groupby(words, first_words):
    print(letter.upper(), list(words))


path = r"~\Desktop\Github_Package\Data-Analysis"
f = open(path, 'w')
try:
    write_to_file(f)
except:
    print('Failed')
else:
    print('succeeded')
finally:
    f.close()


import sys
sys.getdefaultencoding()

