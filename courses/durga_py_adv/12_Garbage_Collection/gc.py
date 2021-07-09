import time
class Test:
    def __init__(self):
        print('Object Initialization...')
        
    def __del__(self):
        print('Fullfilling last wish and performing cleanup activities...')
        
t1=Test()
#t1=None
#t1=None
time.sleep(10)
print('End of application...')