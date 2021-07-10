#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017681679479008

# namedtuple是一个函数，
# 它用来创建一个自定义的tuple对象，
# 并且规定了tuple元素的个数，
# 并可以用属性而不是索引来引用tuple的某个元素。
#
# 这样一来，我们用namedtuple可以很方便地定义一种数据类型，
# 它具备tuple的不变性，又可以根据属性来引用，使用十分方便。

from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import Counter

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print('Point:', p.x, p.y)

# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，
# 因为list是线性存储，数据量大的时候，插入和删除效率很低。
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
# deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，
# 这样就可以非常高效地往头部添加或删除元素。

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

# 使用dict时，如果引用的Key不存在，就会抛出KeyError。
# 如果希望key不存在时，返回一个默认值，就可以用defaultdict：

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print('dd[\'key1\'] =', dd['key1'])
print('dd[\'key2\'] =', dd['key2'])

# Counter是一个简单的计数器，例如，统计字符出现的个数：
# Counter实际上也是dict的一个子类，上面的结果可以看出每个字符出现的次数。

c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)
