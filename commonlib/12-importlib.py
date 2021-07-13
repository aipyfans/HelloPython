import importlib

# 正常导入
module = importlib.import_module('12-importlib.submodule')
print(module)

# 重新载入已有模块
model2 = importlib.reload(module)
print(model2)

# 异常导入
try:
    nomodule = importlib.import_module('12-importlib.nomodule')
    print(nomodule)
except ImportError as err:
    print('Error:', err)
