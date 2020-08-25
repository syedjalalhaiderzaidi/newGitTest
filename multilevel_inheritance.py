"""
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
"""

class Family:
    def __init__(self): 
        print('HEY !!!!!! I am initialised(Class Family)') 
    def show_family(self):
        print("This is our family:")
 
 
# Father class inherited from Family
class Father(Family):
    fathername = ""
    def __init__(self): 
        print('HEY !!!!!!I am initialised(Class Father)') 
        super().__init__()
    
    def show_father(self):
        print(self.fathername)
 
 
# Mother class inherited from Family
class Mother(Family):

    mothername = ""
    def __init__(self): 
        print('HEY !!!!!!I am initialised(Class Mother)') 
        super().__init__()
 
    def show_mother(self):
        print(self.mothername)
 
 
# Son class inherited from Father and Mother classes
class Son(Father, Mother):
    def __init__(self): 
        print('HEY !!!!!!I am initialised(Class Son)') 
        super().__init__()
  
    def show_parent(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)
 
 
s1 = Son()  # Object of Son class
s1.fathername = "Mark"
s1.mothername = "Sonia"
s1.show_family()
s1.show_father()
s1.show_mother()
s1.show_parent()
 