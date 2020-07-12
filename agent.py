from playsound import playsound
"""
Tracker

Date: July 11, 2020
Author: Karen Urate
File: agent.py
Description: This file contains the class objects for Tracker.

------------------------------------------------------------------
                           PROJECT DESCRIPTION
------------------------------------------------------------------
Create a knowledge-based agent prototype that will compute and trace
the source of infection for an individual who has contracted Covid-19
disease from Location 1 to Location 6 in a span of 12-hour period on
9th of January 2019, based on fictional raw data provided.

The agent must have an ability to learn, create new models,
and find the source of infection based on built-up knowledge base.
"""

class Agent():
    def __init__(self, greeting, name):
        self.id = "A00"
        self.greeting = greeting
        self.name = name
        self.models = []
        self.library = []
        self.individual = Individual()

    def collect(self,information):
        self.library.append(information)

    def find(self):
        return None

    def learn(self):
        return None

    def greet(self):
        referral = input(self.greeting)
        self.individual.name = referral
        print("Hello, " + self.individual.name + "!")

    def interrogate(self,probe_id):
        points = input(probe_id)

class Individual:
    def __init__(self,name=""):
        self.id = 0
        self.name = name

class Location:
    def __init__(self,id=0,quarantines=[]):
        self.id = id
        self.quarantines = quarantines

    def match(self, location):
        for p in location.quarantines:
            if p in self.quarantines:
                return True

        return False

    def print(self):
        print("Location " + str(self.id) + ": " + str(self.quarantines))

class Model:
    def __init__(self,knowledge):
        self.id = 0
        self.knowledge = knowledge

    def match(self, model):
        base = model.knowledge.base

        for i in base:
            if i not in self.knowledge.base:
                return False

        return True

class Knowledge:
    def __init__(self,location,contact,visit):
        self.id = 0
        self.location = location
        self.contact = contact
        self.visit = visit

    def process(self, information):
        return None