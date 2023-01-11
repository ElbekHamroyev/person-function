# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 00:46:30 2023

@author: user
"""

class Person:
    def __init__(self):
        self.name = input("What is your name? ")
        self.age = self.get_age()
        self.height = self.get_height()
        self.where = self.get_where_are_you()
        self.school = self.get_school()
    def get_age(self):
        age = input("How old are you? ")
        try:
            age = int(age)
            return age
        except ValueError:
            print("Invalid age. Please enter a valid number.")
            return self.get_age()

    def get_height(self):
        height = input("How tall are you (in meters)? ")
        try:
            height = float(height)
            return height
        except ValueError:
            print("Invalid height. Please enter a valid number.")
            return self.get_height()
    def get_where_are_you(self):
        where = input("where are you from? ")
        try:
            return where
        except ValueError:
            print("you are  entered wrong country name ")
            return self.get_where_are_you()
    def get_school(self):
        school = input("which school did you graduate from? ")
        try:
            school = int(school)
            return school
        except ValueError:
            print("you are  entered wrong shool number")
            return self.get_school_number()
person = Person()
print(f"Name: {person.name}\nAge: {person.age}\nHeight: {person.height}\nCountry: {person.where}\nSchool: {person.school}")