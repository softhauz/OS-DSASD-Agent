from playsound import playsound
from probes import *
from location import *

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
                if any(place == i.strip() for place in points[0].quarantines) and (M004 not in prober):
                    prober.append(M004)
                if any(place == i.strip() for place in points[1].quarantines) and (M005 not in prober):
                    prober.append(M005)
                if any(place == i.strip() for place in points[2].quarantines) and (M006 not in prober):
                    prober.append(M006)
                if any(place == i.strip() for place in points[3].quarantines) and (M007 not in prober):
                    prober.append(M007)
                if any(place == i.strip() for place in points[5].quarantines) and (M008 not in prober):
                    prober.append(M008)

            return prober

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

    def reply(self,message):
        print("[Agent "+self.name+"]:" + message)

    def greet(self):
        referral = input(self.greeting)
        self.individual.name = referral
        print("Hello, " + self.individual.name + "!")

    def interrogate(self,probe_id=""):
        return input("[Agent "+self.name+"]:" + probe_id)

    def validate(self,type=0,information=[]):

        def validate_location(information):
            valid = False
            information = information.split()

            for i in information:
                try:
                    test = int(i)
                    if isinstance(test, int):
                        valid = True
                    break
                except:
                    continue

            return valid

        if type == TYPE_LOCATION:
            return validate_location(information)

    def process(self,type=0,information=[]):

        # process data
        if type == TYPE_LOCATION:

            if not self.validate(TYPE_LOCATION, information):
                return ERR_LOCATION_NOT_INDICATED
            else:
                return self.process_locations()

        # collect locations
        def process_locations():
            data = self.interrogate(M001)
            state = self.process(TYPE_LOCATION,data)
            original = data
            loc_filter = self.find(TYPE_LOCATION,original)

            # find valid location
            if state == ERR_LOCATION_NOT_INDICATED:
                data = self.interrogate(M002)
                state = self.process(TYPE_LOCATION,data)
                i = 0

                if state == ERR_LOCATION_NOT_INDICATED and len(loc_filter) > 0:
                    self.reply(M003)
                    self.reply(M012)
                    self.reply(original)

                    while (state == ERR_LOCATION_NOT_INDICATED) and (i < len(loc_filter)):
                        answer = self.interrogate(loc_filter[i])

                        if answer.strip().lower() in AFFIRMATIONS:
                            data = str(self.find(TYPE_RESPONSE_LOCATION,loc_filter[i]))

                        state = self.process(TYPE_LOCATION,data)
                        i = i + 1

                    if state == ERR_LOCATION_NOT_INDICATED:
                        self.reply(M009)
                        exit
                    elif state == ERR_NOT_COMPROMISED:
                        self.reply(M010)
                    else:
                        self.reply(M011)

                elif state == ERR_LOCATION_NOT_INDICATED and len(loc_filter) == 0:
                    self.reply(M010)

    def collect(self,type=0,information=[]):

        if type == TYPE_LOCATION:

            places = information.split()
            visited = []
            location = Location()
            last = 0

            try:
                last = int(places[len(places) - 1])
            except:
                answer = self.interrogate(M013)

            for p in places:
                try:
                    location.id = int(p)
                    visited.append(location)
                    location = Location(0, [])
                except:
                    location.quarantines.append(p)
                    continue


            return visited

    def learn(self):
        return None

class Individual:
    def __init__(self,name=""):
        self.id = 0
        self.name = name

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