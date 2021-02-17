# Mariska de Vries
# 223751
# 15-1-2021
# Student

class Student:
    def __init__(self, naam, studentennummer, klas, opleiding):
        self.naam = naam
        self.studentennummer = studentennummer
        self.klas = klas
        self.opleiding = opleiding

    def printen(self):
        print(f'Naam student: {self.naam} \nStudentennummer: {self.studentennummer} \nOpleiding: {self.opleiding} \nKlas: {self.klas}')


student = Student('Mariska', '223751', 'ITGO20DEV', 'Software developer')

student.printen()