class Student:
  def  __init__(self,name,roll_number,cgpa):
    self.name=name 
    self.roll_number = roll_number 
    self.cgpa=cgpa
def sort_students(student_list)  : 
  sorted_students = sorted ( student_list,key=lambda student:  student.cgpa ,reverse =True)
  return sorted_students
Students = [  Student("Hari","A123",7.8)    ,Student("Srikanth","A124",8.3)    ,Student("soumya","A125",9.1)      ,Student("Mahesh","A126",9.9)]
sorted_students = sort_students (Students )
for student in sorted_students:
  print("Name : {} ,Roll Number : {} ,CGPA : {} ".format (     student.name , student.roll_number, student.cgpa))
