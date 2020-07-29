import data
from data import *
from knowledge import *
from probes import *

"""

Simultaneous Tracker: "Historian"

Date: July 11, 2020
Author: Karen Urate
File: model.py
Description: This file contains the class object representation for Model.


------------------------------------------------------------------
                           PROJECT DESCRIPTION
------------------------------------------------------------------
Create a knowledge-based agent prototype that will compute and trace
for the source of infection for an individual who has contracted Covid-19
disease from Location 1 to Location 6 in a span of 12-hour period on
9th of January 2020, based on fictional raw data provided.

The agent must have an ability to learn, create new models,
and find the source of infection based on built-up knowledge base.

Upon acquiring sufficient knowledge, the agent must be able to find
the following: where the exact source of infection took place,
from whom the viral infection possibly came from, and which location category
the virus had been spread from.

"""
class Model:

    def __init__(self, knowledge=None, message=""):
        self.id = 0
        self.knowledge = knowledge
        self.message = message

    def match(self, model=None):
        if (self.location.match(model.knowledge.location)) and \
            (any(self.knowledge.contacts == c for c in model.knowledge.contacts)) and \
            (self.knowledge.area == model.knowledge.area):
            return True

        return False

    def print(self):
        self.knowledge.print()

    def check(self,models=[]):

        found = True

        for m in models:
            not_found = False

            if self.knowledge.location.id == m.knowledge.location.id and \
                    self.knowledge.area == m.knowledge.area:

                if any(c not in m.knowledge.contacts for c in self.knowledge.contacts):
                    continue

                for mc in m.knowledge.contacts:
                    if (mc not in self.knowledge.contacts):
                        not_found = True
                        break

                if not_found:
                    continue
                else:
                    self.message = m.message
                    break
            else:
                continue

        if found:
            print(self.message)
        else:
            self.print()
            print("There is no available AI model for the user's case.")

    def compute(self,agent=None,QUARANTINES=[],MODELS=[]):
        found = False
        DENY = data.DENY
        location = data.Location()

        for v in agent.individual.visits:
            location = v
            flag_1 = False

            # Probe for every visited area in current location (v)
            # arrange chronology based on timeline regardless of input
            for place in v.quarantines:

                # LOCATION 1 - OFFICE [1st event]
                if v.id == 1 and (place.find("office") > -1 or "office" in v.quarantines) and (not flag_1):
                    answer = agent.interrogate(M038)

                    if answer not in AFFIRMATIONS:
                        flag_1 = True
                        continue # source did not come from this place

                    answer = agent.interrogate(M018)

                    if answer not in AFFIRMATIONS:
                        agent.individual.source = "AA, BA, or CA"
                        agent.individual.model.knowledge = Knowledge(QUARANTINES[0],["AA","BA","CA"],"office")
                        agent.individual.model.check(MODELS)
                        found = True
                        break # source is found
                    else:
                        answer = DENY
                        prober = [M019, M020, M021]
                        possibilities = ["AA", "BA", "CA"]
                        i = 0

                        while answer not in AFFIRMATIONS and (i < len(prober)):
                            answer = agent.interrogate(prober[i])
                            i = i + 1

                            if answer in AFFIRMATIONS:
                                break

                        i = i - 1

                        if answer not in AFFIRMATIONS:
                            agent.individual.source = "AA, BA, or CA"
                            agent.individual.model.knowledge = Knowledge(QUARANTINES[0], ["AA", "BA", "CA"], "office")
                            agent.individual.model.check(MODELS)
                            found = True
                            break  # source is found
                        else:
                            agent.individual.source = possibilities[i]
                            agent.individual.model.knowledge = Knowledge(QUARANTINES[0], [possibilities[i]], "office")
                            agent.individual.model.check(MODELS)
                            found = True
                            break  # source is found

                # LOCATION 1 - GYM [2nd event - same timeline as the rest of compromised areas at Location 1]
                elif v.id == 1 and (place.find("gym") > -1 or "gym" in v.quarantines) and (flag_1 or (place.find("office") not in v.quarantines)):
                    answer = agent.interrogate(M022)

                    if answer not in AFFIRMATIONS:
                        continue
                    else:
                        agent.individual.source = "DA"
                        agent.individual.model.knowledge = Knowledge(QUARANTINES[0],["DA"],"gym")
                        agent.individual.model.check(MODELS)
                        found = True
                        break # source is found

                # LOCATION 1 - GROCERY STORE [2nd event - same timeline as the rest of compromised areas at Location 1]
                elif v.id == 1 and (place.find("grocery") > -1 or place.find("store") > -1) and (flag_1 or (place.find("office") not in v.quarantines)):
                    answer = agent.interrogate(M023)

                    if answer not in AFFIRMATIONS:
                        continue # source did not come from this place
                    else:
                        agent.individual.source = "EA"
                        agent.individual.model.knowledge = Knowledge(QUARANTINES[0],["EA"],"grocery store")
                        agent.individual.model.check(MODELS)
                        found = True
                        break # source is found

                # LOCATION 1 - HOUSE [2nd event - same timeline as the rest of compromised areas at Location 1]
                elif v.id == 1 and (place.find("house") > -1 or place.find("home") > -1) and (flag_1 or (place.find("office") not in v.quarantines)):
                    answer = agent.interrogate(M024)

                    if answer not in AFFIRMATIONS:
                        continue # source did not come from this place
                    else:
                        answer = agent.interrogate(M018)

                        if answer not in AFFIRMATIONS:
                            agent.individual.source = "BA or CA"
                            agent.individual.model.knowledge = Knowledge(QUARANTINES[0],["BA","CA"],"house")
                            agent.individual.model.check(MODELS)
                            found = True
                            break # source is found
                        else:
                            answer = DENY
                            prober = [M026, M027, M028]
                            possibilities = ["BA", "CA", "BA or CA"]
                            i = 0

                            while answer not in AFFIRMATIONS and (i < len(prober)):
                                answer = agent.interrogate(prober[i])
                                i = i + 1

                            i = i - 1

                            if answer not in AFFIRMATIONS:
                                agent.individual.source = "BA or CA"
                                agent.individual.model.knowledge = Knowledge(QUARANTINES[0], ["BA", "CA"], "house")
                                agent.individual.model.check(MODELS)
                                found = True
                                break  # source is found
                            else:
                                agent.individual.source = possibilities[i]
                                agent.individual.model.knowledge = Knowledge(QUARANTINES[0], [possibilities[i]], "house")
                                agent.individual.model.check(MODELS)
                                found = True
                                break  # source is found

                # LOCATION 2 - HOUSE
                elif v.id == 2 and (place.find("house") > -1 or place.find("home") > -1):
                    answer = agent.interrogate(M029)

                    if answer not in AFFIRMATIONS:
                        continue  # source did not come from this place
                    else:
                        answer = agent.interrogate(M018)

                        if answer not in AFFIRMATIONS:
                            agent.individual.source = "AB or BB"
                            agent.individual.model.knowledge = Knowledge(QUARANTINES[1],["AB","BB"],"house")
                            agent.individual.model.check(MODELS)
                            found = True
                            break # source is found
                        else:
                            answer = DENY
                            prober = [M030, M031]
                            possibilities = ["AB", "BB"]
                            i = 0

                            while answer not in AFFIRMATIONS and (i < len(prober)):
                                answer = agent.interrogate(prober[i])
                                i = i + 1

                            i = i - 1

                            if answer not in AFFIRMATIONS:
                                agent.individual.source = "AB or BB"
                                agent.individual.model.knowledge = Knowledge(QUARANTINES[1], ["AB", "BB"], "house")
                                agent.individual.model.check(MODELS)
                                found = True
                                break  # source is found
                            else:
                                agent.individual.source = possibilities[i]
                                agent.individual.model.knowledge = Knowledge(QUARANTINES[1], [possibilities[i]], "house")
                                agent.individual.model.check(MODELS)
                                found = True
                                break  # source is found

                # LOCATION 3 - HOUSE
                elif v.id == 3 and (place.find("house") > -1 or place.find("home") > -1):
                    answer = agent.interrogate(M029)

                    if answer not in AFFIRMATIONS:
                        continue  # source did not come from this place
                    else:
                        answer = agent.interrogate(M018)

                        if answer not in AFFIRMATIONS:
                            agent.individual.source = "AB or BB"
                            agent.individual.model.knowledge = Knowledge(QUARANTINES[2],["AB","BB"],"house")
                            agent.individual.model.check(MODELS)
                            found = True
                            break # source is found
                        else:
                            answer = DENY
                            prober = [M030, M031]
                            possibilities = ["AB", "BB"]
                            i = 0

                            while answer not in AFFIRMATIONS and (i < len(prober)):
                                answer = agent.interrogate(prober[i])
                                i = i + 1

                            i = i - 1

                            if answer not in AFFIRMATIONS:
                                agent.individual.source = "AB or BB"
                                agent.individual.model.knowledge = Knowledge(QUARANTINES[2], ["AB", "BB"], "house")
                                agent.individual.model.check(MODELS)
                                found = True
                                break  # source is found
                            else:
                                agent.individual.source = possibilities[i]
                                agent.individual.model.knowledge = Knowledge(QUARANTINES[2], [possibilities[i]], "house")
                                agent.individual.model.check(MODELS)
                                found = True
                                break  # source is found

                # LOCATION 4 - RESTAURANT
                elif v.id == 4 and (place.find("restaurant") > -1 or place.find("dine-in") > -1):
                    answer = agent.interrogate(M032)

                    if answer not in AFFIRMATIONS:
                        continue  # source did not come from this place
                    else:
                        answer = agent.interrogate(M018)

                        if answer not in AFFIRMATIONS:
                            agent.individual.source = "CB or EB"
                            agent.individual.model.knowledge = Knowledge(QUARANTINES[3], ["CB", "EB"], "restaurant")
                            agent.individual.model.check(MODELS)
                            found = True
                            break  # source is found
                        else:
                            answer = DENY
                            prober = [M033, M034]
                            possibilities = ["CB", "EB"]
                            i = 0

                            while answer not in AFFIRMATIONS and (i < len(prober)):
                                answer = agent.interrogate(prober[i])
                                i = i + 1

                            i = i - 1

                            if answer not in AFFIRMATIONS:
                                agent.individual.source = "CB or EB"
                                agent.individual.model.knowledge = Knowledge(QUARANTINES[3], ["CB", "EB"], "restaurant")
                                agent.individual.model.check(MODELS)
                                found = True
                                break  # source is found
                            else:
                                agent.individual.source = possibilities[i]
                                agent.individual.model.knowledge = Knowledge(QUARANTINES[3], [possibilities[i]], "restaurant")
                                agent.individual.model.check(MODELS)
                                found = True
                                break  # source is found

                # LOCATION 6 - CAMPGROUND
                elif v.id == 6 and (place.find("campground") > -1 or place.find("camp") > -1):
                    answer = agent.interrogate(M035)

                    if answer not in AFFIRMATIONS:
                        continue  # source did not come from this place
                    else:
                        answer = agent.interrogate(M018)

                        if answer not in AFFIRMATIONS:
                            agent.individual.source = "Couple 2's Social Circle"
                            agent.individual.model.knowledge = Knowledge(QUARANTINES[5], ["CB", "EB", "six friends"], "campground")
                            agent.individual.model.check(MODELS)
                            found = True
                            break  # source is found
                        else:
                            answer = DENY
                            prober = [M033, M034, M036]
                            possibilities = ["CB", "EB", "six friends"]
                            i = 0

                            while answer not in AFFIRMATIONS and (i < len(prober)):
                                answer = agent.interrogate(prober[i])
                                i = i + 1

                            i = i - 1

                            if answer not in AFFIRMATIONS:
                                agent.individual.source = "Couple 2's Social Circle"
                                agent.individual.model.knowledge = Knowledge(QUARANTINES[5], ["CB", "EB", "six friends"], "campground")
                                agent.individual.model.check(MODELS)
                                found = True
                                break  # source is found
                            else:
                                agent.individual.source = possibilities[i]
                                agent.individual.model.knowledge = Knowledge(QUARANTINES[5], [possibilities[i]], "campground")
                                agent.individual.model.check(MODELS)
                                found = True
                                break  # source is found

            if found:
                break

        if not found:
            contacts = agent.interrogate(M015)
            information = [location, contacts, location.quarantines]
            agent.learn(information)
            print("\tContacts: " + contacts)
