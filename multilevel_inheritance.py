class A: 
    def __init__(self): 
        print('HEY !!!!!! I am initialised(Class A)') 
  
    def func_print(self, b): 
        print('Printing from class A:', b) 
  
# class B inherits the A 
class B(A): 
    def __init__(self): 
        print('HEY !!!!!! I am initialised(Class B)') 
        super().__init__() 
  
    def func_print(self, b): 
        print('Printing from class B:', b) 
        super().func_print(b + 1) 
  
# class C inherits the A ang B both 
class C(B): 
    def __init__(self): 
        print('HEY !!!!!!I am initialised(Class C)') 
        super().__init__()
  
    def func_print(self, b): 
        print('Printing from class C:', b) 
        super().func_print(b + 1) 
  
  
# main function 
if __name__ == '__main__': 
  
    # created the object gfg 
    grandChild = C() 
  
    # calling the function func_print() from class C 
    # which inherits both A and B classes 
    grandChild.func_print(10) 
