#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://www.liaoxuefeng.com/wiki/1016959663602400/1183198304823296

# Python内置的hmac模块实现了标准的Hmac算法，
# 它利用一个key对message计算“杂凑”后的hash，
# 使用hmac算法比标准hash算法更安全，
# 因为针对相同的message，不同的key会产生不同的hash。

import hmac

message = b'Hello World'

key = b'secret'
h = hmac.new(key, message, digestmod='MD5')
print(h.hexdigest())
