from .bash import *

print('This is for python study')
print('imported list')
for f in dir():
    if f.endswith('__') is False or f.startswith('__') is False:
        print(str(f))
