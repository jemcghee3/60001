# Introduction to Computation and Computer Programming Using Python (2021)
# Chapter 10, Finger Exercise 3


# Classes defined in book

import datetime

class Person(object):
    def __init__(self, name):
        """Assumes name a string. Create a person"""
        self._name = name
        try:
            last_blank = name.rindex(' ')
            self._last_name = name[last_blank+1:]
        except:
            self._last_name = name
        self._birthday = None # Error in book code excludes _
    
    def get_name(self):
        """Returns self's full name"""
        return self._name

    def get_last_name(self):
        """Returns self's last name"""
        return self._last_name
    
    def set_birthday(self, birthdate):
        """Assumes birthdate is of type datetime.date
        Sets self's birthday to birthdate"""
        self._birthday = birthdate
    
    def get_age(self):
        """Returns self's current age in days"""
        if self._birthday == None:
            raise ValueError
        return (datetime.date.today() - self._birthday).days
    
    def __lt__(self, other):
        """Assume other a Person
        Returns True if self precedes other in alphabetical
        order, and False otherwise. Comparison is based on last
        names, but if these are the same full names are
        compared."""
        if self._last_name == other._last_name:
            return self._name < other._name
        return self._last_name < other._last_name
    
    def __str__(self):
        """Returns self's name"""
        return self._name

class MIT_Person(Person):
    _next_id_num = 0 #identification number

    def __init__(self, name):
        super().__init__(name)
        self._id_num = MIT_Person._next_id_num
        MIT_Person._next_id_num += 1
    
    def get_id_num(self):
        return self._id_num
    
    def __lt__(self, other):
        return self._id_num < other._id_num

class Student(MIT_Person):
    pass

class UG(Student):
    def __init__(self, name, class_year):
        super().__init__(name)
        self._year = class_year
    
    def get_class(self):
        return self._year

class Grad(Student):
    pass

class Grades(object):

    def __init__(self):
        """Create empty grade book"""
        self._students = []
        self._grades = {}
        self._is_sorted = True
    
    def add_student(self, student):
        """Assumes: student is of type Student
        Add student to the grade book"""
        if student in self._students:
            raise ValueError('Duplicate student')
        self._students.append(student)
        self._grades[student.get_id_num()] = []
        self._is_sorted = False
    
    def add_grade(self, student, grade):
        """Assumes: grade is a float
        Add grade to the list of grades for student"""
        try:
            self._grades[student.get_id_num()].append(grade)
        except:
            raise ValueError('Student not in mapping')
    
    def get_grades(self, student):
        """Return a list of grades for student"""
        try:
            return self._grades[student.get_id_num()][:]
        except:
            raise ValueError('Student not in mapping')
    
    def get_students(self):
        """Return a sorted list of the students in the grade book"""
        if not self._is_sorted:
            self._students.sort()
            self._is_sorted = True
        for s in self._students:
            yield s

# Finger exercise: Add to Grades a generator that meets the
#specification
    def get_students_above(self, grade):
        """Return the students a mean grade > g one at a time"""
        for s in self.get_students():
            if sum(self.get_grades(s))/len(self.get_grades(s)) > grade:
                yield s

book = Grades()
j = Grad('Julie')
l = Grad('Lisa')
k = Grad('Katherine')
book.add_student(j)
book.add_student(l)
book.add_student(k)
book.add_grade(j, 100)
book.add_grade(j, 10)
book.add_grade(j, 0)

book.add_grade(l, 20)
book.add_grade(l, 10)
book.add_grade(l, 1)

book.add_grade(k, 0)
book.add_grade(k, 1)
book.add_grade(k, 19)

for s in book.get_students():
    print(s)
print('')
for s in book.get_students_above(10):
    print(s)