class A:
    def display(self):
        print("I am in A class")
        
class B(A):
    def display2(self):
        print("I am in B class")

class C(B):
    def display3(self):
        print("I am in C class")
ob1=C()
ob1.display()
ob1.display2()
ob1.display3()