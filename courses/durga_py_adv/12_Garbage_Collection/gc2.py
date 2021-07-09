import time
class Test:
    def __init__(self):
        print('Object Initialization...')
        
    def __del__(self):
        print('Fullfilling last wish and performing cleanup activities...')
        
t1=Test()
t2=t1
t3=t2
t4=t3
del t1
time.sleep(10)
print('After  deleting t1 object not destroyed')
del t2
del t3
print('After deleting  t2, t3 still not destroyed')
del t4
time.sleep(10)
print('End of application...')