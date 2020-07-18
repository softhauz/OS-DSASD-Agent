from individual import *
from data import *
from model import *
from location import *


"""
Simultaneous Tracker: "Historian"

Date: July 11, 2020
Author: Karen Urate
File: agent.py
Description: This file contains the class object representation for Agent.
Agent will create and utilize data relations,
and probe and collection information from individuals.

------------------------------------------------------------------
                           PROJECT DESCRIPTION
------------------------------------------------------------------
Create a knowledge-based agent prototype that will compute and trace
for the source of infection for an individual who has contracted Covid-19
disease from Location 1 to Location 6 in a span of 12-hour period on
9th of January 2019, based on fictional raw data provided.

The agent must have an ability to learn, create new models,
compute for data relations, and find the source of infection 
based on built-up knowledge base.

Upon acquiring sufficient knowledge, the agent must be able to find
the following: where the exact source of infection took place,
from whom the viral infection possibly came from, and which location category 
the virus had been spread from.  
"""

TYPE_LOCATION = 1
TYPE_CONTACT = 2
TYPE_SOURCE = 3
TYPE_RESPONSE_LOCATION = 6
TYPE_COMPROMISED_LOCATION = 7
ERR_LOCATION_NOT_INDICATED = 4
ERR_NOT_COMPROMISED = 5

class Agent():

    def __init__(self, greeting="", name=""):
        self.id = "A00"
        self.greeting = greeting
        self.name = name
        self.individual = Individual()

    def find(self, type=TYPE_LOCATION, input=""):
        prober = []

        if type == TYPE_LOCATION:
            input = input.split()

            for i in input:
                i = i.lower().strip()
                if any(place.find(i) > -1 for place in QUARANTINES[0].quarantines) and (M004 not in prober):
                    prober.append(M004)
                if any(place.find(i) > -1 for place in QUARANTINES[1].quarantines) and (M005 not in prober):
                    prober.append(M005)
                if any(place.find(i) > -1 for place in QUARANTINES[2].quarantines) and (M006 not in prober):
                    prober.append(M006)
                if any(place.find(i) > -1 for place in QUARANTINES[3].quarantines) and (M007 not in prober):
                    prober.append(M007)
                if any(place.find(i) > -1 for place in QUARANTINES[5].quarantines) and (M008 not in prober):
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

        elif type == TYPE_SOURCE:
            self.connect()

        return prober

    def reply(self, message):
        print("[Agent "+self.name+"]: " + message)

    def greet(self):
        self.greeting = "[Agent "+self.name+"]: Hi, I'm " \
                        + self.name + "!" + self.greeting
        self.individual.name = input(self.greeting)
        self.reply("Hello, " + self.individual.name + "!")

    def interrogate(self, probe_id=""):
        return input("[Agent "+self.name+"]: " + probe_id)

    def validate(self, type=0, information=[]):

        # validate location
        def validate_location(information):
            valid = False
            information = information.split()

            for i in information:
                try:
                    test = int(i)
                    if isinstance(test, int):
                        valid = True
                    break # at least 1 indicated location
                except:
                    continue

            return valid

        if type == TYPE_LOCATION:
            return validate_location(information)

    def process(self, type=TYPE_LOCATION):

        # get locations
        def get_locations(agent=Agent(), data=""):

            data = data.lower().strip()
            original = data
            probes = agent.find(TYPE_LOCATION, original)
            valid = agent.validate(TYPE_LOCATION, data)

            if not valid:
                data = agent.interrogate(M002)
                valid = agent.validate(TYPE_LOCATION, data)
                i = 0

                if not valid and len(probes) > 0:
                    agent.reply(M003)
                    agent.reply(M012)
                    agent.reply(original)

                    while (not valid) and (i < len(probes)):
                        answer = agent.interrogate(probes[i])

                        if answer.strip().lower() in AFFIRMATIONS:
                            data = str(agent.find(TYPE_RESPONSE_LOCATION, probes[i]))

                        valid = agent.validate(TYPE_LOCATION, data)
                        i = i + 1

                    if not valid:
                        state = ERR_LOCATION_NOT_INDICATED
                        agent.reply(M009)
                        exit
                    else:
                        original = SPACE.join((original, data))
                        agent.reply(M011)
                        visited = agent.collect(TYPE_LOCATION, original)
                        compromised_visits = agent.collect(TYPE_COMPROMISED_LOCATION, visited)
                        # print("INPUT: " + original) # DEBUGGER

                        if len(compromised_visits) == 0:
                            agent.reply(M010)
                        else:
                            agent.individual.visits = compromised_visits

                elif not valid and len(probes) == 0:
                    agent.reply(M010)
                else:
                    original = SPACE.join((original, data))
                    agent.reply(M011)
                    visited = agent.collect(TYPE_LOCATION, original)
                    compromised_visits = agent.collect(TYPE_COMPROMISED_LOCATION, visited)

                    if len(compromised_visits) == 0:
                        agent.reply(M010)
                        exit
                    else:
                        agent.individual.visits = compromised_visits

            else:
                agent.reply(M011)
                visited = agent.collect(TYPE_LOCATION, original)
                compromised_visits = agent.collect(TYPE_COMPROMISED_LOCATION, visited)

                if len(compromised_visits) == 0:
                    agent.reply(M010)
                else:
                    agent.individual.visits = compromised_visits
        # end get_locations()

        data = self.interrogate(M001)
        get_locations(self, data)

        ''' DEBUGGER: Print locations from compromised_visits '''
        compromised_visits = self.individual.visits
        if len(compromised_visits) > 0:
            self.reply("On January 9, 2020, the compromised areas that you have visited are:")
            for c in self.individual.visits:
                c.print()

        self.connect()

    def connect(self):
        self.reply(M017)
        self.individual.model = Model()
        self.individual.model.compute(self)

    def collect(self, type=0, information=[]):
        if type == TYPE_LOCATION:

            places = information.split()
            visited = []
            location = Location()
            last = 0

            try:
                last = int(places[len(places) - 1])
            except:
                answer = self.interrogate(M013)
                answer = answer.strip()

                try:
                    places.append(int(answer))
                except:
                    self.reply(M014)

            for p in places:
                try:
                    location.id = int(p)
                    visited.append(location)
                    location = Location(0, [])
                except:
                    location.quarantines.append(p)
                    continue

            return visited

        elif type == TYPE_COMPROMISED_LOCATION:
            visits = information
            compromised_visits = []
            i = 0

            for q in QUARANTINES: # keep order based on timeline
                for v in visits:
                    # if any(q.match(v) for v in visits) and v not in compromised_visits: # alternative | random input allowance
                    if q.match(v) and (v not in compromised_visits):
                        compromised_visits.append(v)

            return compromised_visits

    def learn(self, information=[]):
        f = open("knowledge.txt", "a")
        text = ""

        for i in information:
            if isinstance(i,Location):
                text = text + i.text() + SPACE
            else:
                text = text + str(i) + SPACE

        f.write("\n"+text)
        f.close()
        self.reply(M037)

