from functools import lru_cache
from time import sleep

@lru_cache(maxsize=None)
def fx(n):
    sleep(2)
    return n*5

print(fx(3))
print('done for 3')
print(fx(5))
print('done for 5')
print(fx(8))
print('done for 8')
print('***runnning from cache***')
print(fx(3))
print('done for 3')
print(fx(5))
print('done for 5')
print(fx(8))
print('done for 8')
