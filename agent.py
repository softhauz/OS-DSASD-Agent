from playsound import playsound
from probes import *

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

TYPE_LOCATION = 1
TYPE_CONTACT = 2
TYPE_VISIT = 3
TYPE_RESPONSE_LOCATION = 6
ERR_LOCATION_NOT_INDICATED = 4
ERR_NOT_COMPROMISED = 5


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

    def find(self,type=TYPE_LOCATION,input=""):
        prober = []
        points = [
            Location(1, ["office", "gym", "grocery store", "house"]),
            Location(2, ["home"]),
            Location(3, ["home"]),
            Location(4, ["restaurant"]),
            Location(5, ["park", "beach", "mall"]),
            Location(6, ["campground"])
        ]

        if type == TYPE_LOCATION:
            input = input.split()
            for i in input:
                if any(place == i for place in points[0].quarantines) and (M004 not in prober):
                    prober.append(M004)
                if any(place == i for place in points[1].quarantines) and (M005 not in prober):
                    prober.append(M005)
                if any(place == i for place in points[2].quarantines) and (M006 not in prober):
                    prober.append(M006)
                if any(place == i for place in points[3].quarantines) and (M007 not in prober):
                    prober.append(M007)
                if any(place == i for place in points[5].quarantines) and (M008 not in prober):
                    prober.append(M008)
        elif type == TYPE_RESPONSE_LOCATION:
            if input == M004:
                return 1
            elif input == M005:
                return 2
            elif input == M006:
                return 3
            elif input == M007:
                return 4
            elif input == M008:
                return 6

        return prober

    def learn(self):
        return None

    def reply(self,message):
        print(message)

    def greet(self):
        referral = input(self.greeting)
        # playsound('tester1.wav')
        self.individual.name = referral
        print("Hello, " + self.individual.name + "!")

    def interrogate(self,probe_id):
        return input(probe_id)

    def validate(self,type,information):

        def validate_location(information):
            valid = False
            information = information.split()

            for i in information:
                try:
                    test = int(i)
                    if(isinstance(test,int)):
                        valid = True
                    break
                except:
                    continue

            return valid

        if type == TYPE_LOCATION:
            return validate_location(information)

    def process(self,type=0,information=[]):

        if type == TYPE_LOCATION:

            if not self.validate(TYPE_LOCATION, information):
                return ERR_LOCATION_NOT_INDICATED
            else:
                if(int(information) > 6 or int(information) < 0):
                    return ERR_NOT_COMPROMISED
                else:
                    return -1


class Individual:
    def __init__(self,name=""):
        self.id = 0
        self.name = name

class Location:
    def __init__(self,id=0,quarantines=[]):
        self.id = id
        self.quarantines = quarantines

    def match(self, location=None):

        if self.id == location.id:
            for p in location.quarantines:
                if p in self.quarantines:
                    # print("1st Common Place Found: " + p) #----------- DEBUGGER
                    return True

        return False

    def print(self):
        print("Location " + str(self.id) + ": " + str(self.quarantines))

class Model:
    def __init__(self,knowledge):
        self.id = 0
        self.knowledge = knowledge

    def match(self, model):
        base = model.knowledge
        return True

class Knowledge:
    def __init__(self,location,contact,visit):
        self.id = 0
        self.location = location
        self.contact = contact
        self.visit = visit

    def process(self, information):
        return None