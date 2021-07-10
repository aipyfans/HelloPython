#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017783145987360

# itertools模块提供的全部是处理迭代功能的函数，
# 它们的返回值不是list，而是Iterator，
# 只有用for循环迭代的时候才真正计算。

import itertools

natuals = itertools.count(1)
for n in natuals:
    print(n)
    if n >= 10:
        break

print('--------------------------')

cs = itertools.cycle('ABC')
t = 10
for c in cs:
    print(c)
    t = t - 1
    if t == 0:
        break

print('--------------------------')

ns = itertools.repeat('A', 3)
for m in ns:
    print(m)

print('--------------------------')

natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))

print('--------------------------')

for c in itertools.chain('ABC', 'XYZ'):
    print(c)

print('--------------------------')

for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))

print('--------------------------')

for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))
