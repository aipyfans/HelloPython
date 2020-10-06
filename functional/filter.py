#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# filter()的作用是从一个序列中筛出符合条件的元素。
# 由于filter()使用了惰性计算，所以只有在取filter()结果的时候，才会真正筛选并每次返回下一个筛出的元素。
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017404530360000

def is_odd(n):
    return n % 2 == 1


L = range(10)

print(list(filter(is_odd, L)))


def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))
