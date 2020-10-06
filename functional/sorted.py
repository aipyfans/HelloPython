#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# sorted()也是一个高阶函数。用sorted()排序的关键在于实现一个映射函数。
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017408670135712

from operator import itemgetter

L = ['bob', 'about', 'Zoo', 'Credit']

print(sorted(L))
print(sorted(L, key=str.lower))

students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(sorted(students, key=itemgetter(0)))
print(sorted(students, key=lambda t: t[1]))
print(sorted(students, key=itemgetter(1), reverse=True))
