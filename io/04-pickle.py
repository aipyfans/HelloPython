#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017624706151424

import pickle

d = dict(name='william', age=21, score=88)
data = pickle.dumps(d)
print(data)

reborn = pickle.loads(data)
print(reborn)


class Student(object):

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return 'Student object (%s, %s, %s)' % (self.name, self.age, self.score)


s = Student('Bob', 20, 88)
std_data = json.dumps(s, default=lambda obj: obj.__dict__)
print('Dump Student:', std_data)
rebuild = json.loads(std_data, object_hook=lambda d: Student(d['name'], d['age'], d['score']))
print(rebuild)
