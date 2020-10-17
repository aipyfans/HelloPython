#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017628290184064
import os

print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))