class A:
    def display(self):
        print("I am in A class")
        
class B:
    def display(self):
        print("I am in B class")

class C(A,B):
    def display(self):
        print("I am in C class")
ob1=C()
ob1.display()