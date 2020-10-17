#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017628290184064
# 控制子进程的输入和输出

import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
