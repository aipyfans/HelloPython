"""
redis://[:password]@host:port/db
rediss://[:password]@host:port/db
unix://[:password]@/path/to/socket.sock?db=db
"""

from redis import StrictRedis, ConnectionPool

# redis = StrictRedis(host='localhost', port=6379, db=0, password=None)

# pool = ConnectionPool(host='localhost', port=6379, db=0, password=None)
# redis = StrictRedis(connection_pool=pool)

url = 'redis://localhost:6379/0'
pool = ConnectionPool.from_url(url)
redis = StrictRedis(connection_pool=pool)

# 给数据库中键为name的string赋予值value
redis.set('name', 'William')

# 返回数据库中键为name的string的value
name = redis.get('name')
print(name)
print('-'.join(name.decode('utf-8')))

# 键操作

print("判断一个键是否存在")
print(redis.exists('name'))

print("判断键类型")
print(redis.type('name'))

print("获取所有符合规则的键")
print(redis.keys('*'))

print("删除一个键")
print(redis.delete('name'))
