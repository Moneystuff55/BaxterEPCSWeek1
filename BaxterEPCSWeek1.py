import math
import random

def main():
  students = [
    Student("Larsson","Hal", 37,100,60),
    Student("BonJovi","Jon", 55,100,60),
    Student("Link"," ", 117,100,60),
  ]

  printHeader()
  selection = getUserSelection()
  if selection == "0":
    printStudentsByAge(students)
  elif selection == "1":
    printStudentsByLName(students)
  elif selection == "2":
    printStudentsByFName(students)
  elif selection == "3":
    printSumAge(students)
  elif selection == "4":
    printAvgAge(students)
  else:
    print ("SELECTION NOT RECOGNIZED")


class Student:
  def __init__(self, lastName,firstName,age,weight,height):
    self.assignRandomAge()
    self.assignRandomWeight()
    self.assignRandomHeight()
    self.assignRandomFName()
    self.assignRandomLName()

  def assignRandomFName(self):
    firstName = ["Bob","Jim","Tom","Timmy","Zach","Larry","Jimmy","Jerome"]
    lastName = ["smith","pillsbury","dussault","person","cadigan"]
    self.firstName = firstName[random.randint(0,7)]
   

  def assignRandomLName(self):
    lastName = ["smith","pillsbury","dussault","person","cadigan"]
    self.lastName = lastName[random.randint(0,4)]

  def assignRandomAge(self):
    self.age = random.randint(1,300)

  def assignRandomWeight(self):
    self.weight = random.randint(100,200)

  def assignRandomHeight(self):
    self.height = random.randint(0,84)

inputQuestions = [ 
  "For STUDENTS BY AGE, type 0",
  "For STUDENTS BY LAST NAME, type 1",
  "For STUDENTS BY FIRST NAME, type 2",
  "For SUM of STUDENT AGES type 3",
  "For AVERAGE of STUDENT AGES type 4",
]

def getUserSelection():
  for inputQuestion in inputQuestions:
    print(inputQuestion)
  return str(input("Type selection and press enter:"))

def printHeader():
    print("HEADER TEXT HERE")

def printStudentsByAge(students):
  print ("----Students By Age-----")
  sortStudents = sorted(students, key=lambda student: student.age)
  for student in sortStudents:
   print (student.lastName + ", " + student.firstName + ", " + str(student.age) + "," + str(student.weight) + "," + str(student.height))


def printStudentsByLName(students):
  print ("----Students By -----")
  sortStudents = sorted(students, key=lambda student: student.lastName)
  for student in sortStudents:
      print (student.lastName + ", " + student.firstName + ", " + str(student.age) + "," + str(student.weight) + "," + str(student.height))

def printStudentsByFName(students):
  print ("----Students By -----")
  sortStudents = sorted(students, key=lambda student: student.firstName)
  for student in sortStudents:
      print (student.lastName + ", " + student.firstName + ", " + str(student.age) + "," + str(student.weight) + "," + str(student.height))

def printSumAge(students):
  print ("Answer:")
 for student in students:
  totalAge = student + totalAge
  print (totalAge)

def printAvgAge(students):
  print ("Answer:")


def ageRange(studentA, studentB):
  return math.abs(studentA.age - studentB.age)


main()
