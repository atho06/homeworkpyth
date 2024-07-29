#Create a class "Student" with attributes: name, roll_number, and grades. Write a method to calculate the average grade.
class Student:
    def __init__(self, n, roll, grd):
        self.name=str(n)
        self.roll_number=int(roll)
        self.grades=list(grd)
    def avg_grade(self):
        total=0
        for i in self.grades:
            total+=i
        return total/len(self.grades)

#MAIN
name=input("Enter name:")
roll=int(input("Enter roll number:"))
grades=[]
print("Enter grades(enter 999.9 to stop):")
while True:
    grd=float(input("Enter grade:"))
    if grd==999.9:
        break
    grades.append(grd)
avg=Student(name, roll, grades)
print("average",name, "scored: " ,avg.avg_grade())  
