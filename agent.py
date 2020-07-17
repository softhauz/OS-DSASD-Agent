from probes import *
from individual import *
from data import *

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
and find the source of infection based on built-up knowledge base.

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
SPACE = " "
DENY = "No"

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

        self.individual.model = Model()
        self.connect()

    def connect(self):
        self.reply(M017)
        found = False

        for v in self.individual.visits:

            # Probe for every visited area in current location (v)
            for place in v.quarantines:

                # LOCATION 1 - OFFICE
                if place in QUARANTINES[0].quarantines and v.id == 1 and place == "office":
                    answer = self.interrogate(M018)

                    if answer not in AFFIRMATIONS:
                        self.individual.source = "AA, BA, or CA"
                        self.individual.model.knowledge = Knowledge(QUARANTINES[0],["AA","BA","CA"],"office")
                        self.individual.model.check(MODELS)
                        found = True
                        break # source is found
                    else:
                        answer = DENY
                        prober = [M019, M020, M021]
                        possibilities = ["AA", "BA", "CA"]
                        i = 0

                        while answer not in AFFIRMATIONS and (i < len(prober)):
                            answer = self.interrogate(prober[i])
                            i = i + 1

                        i = i - 1

                        if answer not in AFFIRMATIONS:
                            self.individual.source = "AA, BA, or CA"
                            self.individual.model.knowledge = Knowledge(QUARANTINES[0], ["AA", "BA", "CA"], "office")
                            self.individual.model.check(MODELS)
                            found = True
                            break  # source is found
                        else:
                            self.individual.source = possibilities[i]
                            self.individual.model.knowledge = Knowledge(QUARANTINES[0], [possibilities[i]], "office")
                            self.individual.model.check(MODELS)
                            found = True
                            break  # source is found

                # LOCATION 1 - GYM
                elif place in QUARANTINES[0].quarantines and v.id == 1 and place == "gym":
                    answer = self.interrogate(M022)

                    if answer not in AFFIRMATIONS:
                        continue
                    else:
                        self.individual.source = "DA"
                        self.individual.model.knowledge = Knowledge(QUARANTINES[0],["DA"],"gym")
                        self.individual.model.check(MODELS)
                        found = True
                        break # source is found

                # LOCATION 1 - GROCERY STORE
                elif place in QUARANTINES[0].quarantines and v.id == 1 and (place.find("grocery") > -1 or place.find("store") > -1):
                    answer = self.interrogate(M023)

                    if answer not in AFFIRMATIONS:
                        continue # source did not come from this place
                    else:
                        self.individual.source = "EA"
                        self.individual.model.knowledge = Knowledge(QUARANTINES[0],["EA"],"grocery store")
                        self.individual.model.check(MODELS)
                        found = True
                        break # source is found

                # LOCATION 1 - HOUSE
                elif place in QUARANTINES[0].quarantines and v.id == 1 and (place.find("house") > -1 or place.find("home") > -1):
                    answer = self.interrogate(M024)

                    if answer not in AFFIRMATIONS:
                        continue # source did not come from this place
                    else:
                        answer = self.interrogate(M018)

                        if answer not in AFFIRMATIONS:
                            self.individual.source = "BA or CA"
                            self.individual.model.knowledge = Knowledge(QUARANTINES[0],["BA","CA"],"house")
                            self.individual.model.check(MODELS)
                            found = True
                            break # source is found
                        else:
                            answer = DENY
                            prober = [M026, M027, M028]
                            possibilities = ["BA", "CA", "BA or CA"]
                            i = 0

                            while answer not in AFFIRMATIONS and (i < len(prober)):
                                answer = self.interrogate(prober[i])
                                i = i + 1

                            i = i - 1

                            if answer not in AFFIRMATIONS:
                                self.individual.source = "BA or CA"
                                self.individual.model.knowledge = Knowledge(QUARANTINES[0], ["BA", "CA"], "house")
                                self.individual.model.check(MODELS)
                                found = True
                                break  # source is found
                            else:
                                self.individual.source = possibilities[i]
                                self.individual.model.knowledge = Knowledge(QUARANTINES[0], [possibilities[i]], "house")
                                self.individual.model.check(MODELS)
                                found = True
                                break  # source is found

                # LOCATION 2 - HOUSE
                elif place in QUARANTINES[1].quarantines and v.id == 2 and (place.find("house") > -1 or place.find("home") > -1):
                    answer = self.interrogate(M029)

                    if answer not in AFFIRMATIONS:
                        continue  # source did not come from this place
                    else:
                        answer = self.interrogate(M018)

                        if answer not in AFFIRMATIONS:
                            self.individual.source = "AB or BB"
                            self.individual.model.knowledge = Knowledge(QUARANTINES[1],["AB","BB"],"house")
                            self.individual.model.check(MODELS)
                            found = True
                            break # source is found
                        else:
                            answer = DENY
                            prober = [M030, M031]
                            possibilities = ["AB", "BB"]
                            i = 0

                            while answer not in AFFIRMATIONS and (i < len(prober)):
                                answer = self.interrogate(prober[i])
                                i = i + 1

                            i = i - 1

                            if answer not in AFFIRMATIONS:
                                self.individual.source = "AB or BB"
                                self.individual.model.knowledge = Knowledge(QUARANTINES[1], ["AB", "BB"], "house")
                                self.individual.model.check(MODELS)
                                found = True
                                break  # source is found
                            else:
                                self.individual.source = possibilities[i]
                                self.individual.model.knowledge = Knowledge(QUARANTINES[1], [possibilities[i]], "house")
                                self.individual.model.check(MODELS)
                                found = True
                                break  # source is found

                # LOCATION 3 - HOUSE
                elif place in QUARANTINES[2].quarantines and v.id == 3 and (place.find("house") > -1 or place.find("home") > -1):
                    answer = self.interrogate(M029)

                    if answer not in AFFIRMATIONS:
                        continue  # source did not come from this place
                    else:
                        answer = self.interrogate(M018)

                        if answer not in AFFIRMATIONS:
                            self.individual.source = "AB or BB"
                            self.individual.model.knowledge = Knowledge(QUARANTINES[2],["AB","BB"],"house")
                            self.individual.model.check(MODELS)
                            found = True
                            break # source is found
                        else:
                            answer = DENY
                            prober = [M030, M031]
                            possibilities = ["AB", "BB"]
                            i = 0

                            while answer not in AFFIRMATIONS and (i < len(prober)):
                                answer = self.interrogate(prober[i])
                                i = i + 1

                            i = i - 1

                            if answer not in AFFIRMATIONS:
                                self.individual.source = "AB or BB"
                                self.individual.model.knowledge = Knowledge(QUARANTINES[2], ["AB", "BB"], "house")
                                self.individual.model.check(MODELS)
                                found = True
                                break  # source is found
                            else:
                                self.individual.source = possibilities[i]
                                self.individual.model.knowledge = Knowledge(QUARANTINES[2], [possibilities[i]], "house")
                                self.individual.model.check(MODELS)
                                found = True
                                break  # source is found

                # LOCATION 4 - RESTAURANT
                elif place in QUARANTINES[3].quarantines and v.id == 4 and (place.find("restaurant") > -1 or place.find("dine-in") > -1):
                    answer = self.interrogate(M032)

                    if answer not in AFFIRMATIONS:
                        continue  # source did not come from this place
                    else:
                        answer = self.interrogate(M018)

                        if answer not in AFFIRMATIONS:
                            self.individual.source = "CB or EB"
                            self.individual.model.knowledge = Knowledge(QUARANTINES[3], ["CB", "EB"], "restaurant")
                            self.individual.model.check(MODELS)
                            found = True
                            break  # source is found
                        else:
                            answer = DENY
                            prober = [M033, M034]
                            possibilities = ["CB", "EB"]
                            i = 0

                            while answer not in AFFIRMATIONS and (i < len(prober)):
                                answer = self.interrogate(prober[i])
                                i = i + 1

                            i = i - 1

                            if answer not in AFFIRMATIONS:
                                self.individual.source = "CB or EB"
                                self.individual.model.knowledge = Knowledge(QUARANTINES[2], ["CB", "EB"], "restaurant")
                                self.individual.model.check(MODELS)
                                found = True
                                break  # source is found
                            else:
                                self.individual.source = possibilities[i]
                                self.individual.model.knowledge = Knowledge(QUARANTINES[2], [possibilities[i]], "restaurant")
                                self.individual.model.check(MODELS)
                                found = True
                                break  # source is found

                # LOCATION 6 - CAMPGROUND
                elif place in QUARANTINES[5].quarantines and v.id == 6 and (place.find("campground") > -1 or place.find("camp") > -1):
                    answer = self.interrogate(M035)

                    if answer not in AFFIRMATIONS:
                        continue  # source did not come from this place
                    else:
                        answer = self.interrogate(M018)

                        if answer not in AFFIRMATIONS:
                            self.individual.source = "Couple 2's Social Circle"
                            self.individual.model.knowledge = Knowledge(QUARANTINES[5], ["CB", "EB", "six friends"], "campground")
                            self.individual.model.check(MODELS)
                            found = True
                            break  # source is found
                        else:
                            answer = DENY
                            prober = [M033, M034, M036]
                            possibilities = ["CB", "EB", "six friends"]
                            i = 0

                            while answer not in AFFIRMATIONS and (i < len(prober)):
                                answer = self.interrogate(prober[i])
                                i = i + 1

                            i = i - 1

                            if answer not in AFFIRMATIONS:
                                self.individual.source = "Couple 2's Social Circle"
                                self.individual.model.knowledge = Knowledge(QUARANTINES[5], ["CB", "EB", "six friends"], "campground")
                                self.individual.model.check(MODELS)
                                found = True
                                break  # source is found
                            else:
                                self.individual.source = possibilities[i]
                                self.individual.model.knowledge = Knowledge(QUARANTINES[5], [possibilities[i]], "campground")
                                self.individual.model.check(MODELS)
                                found = True
                                break  # source is found

            if found:
                break

        if not found:
            contacts = self.interrogate(M015)
            information = [v, contacts, v.quarantines]
            self.learn(information)

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

            for v in visits:
                for q in QUARANTINES:
                    if v.match(q) and (v not in compromised_visits):
                        compromised_visits.append(v)

            return compromised_visits

    def learn(self, information=[]):
        f = open("knowledge.txt", "a")
        f.write(str(information))
        f.close()

