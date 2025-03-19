class student:
    roll=" "
    gpa=" "
    def __init__(self,roll,gpa):
        self.roll=roll
        self.gpa=gpa
        
    def display(self):
        print(f"Roll: {self.roll}\nGPA: {self.gpa}")
rahim=student(101,4.6)
rahim.display()