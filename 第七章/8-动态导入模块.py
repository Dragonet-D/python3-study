# mod = __import__('lib.aa')  # 这是解释器自己内部用的  lib
# print(mod)
# instance = getattr(mod.aa, 'C')
# obj = instance()
# print(obj.name)

# 官方建议用这个
import importlib
lib = importlib.import_module('lib.aa')
print(lib.C().name)