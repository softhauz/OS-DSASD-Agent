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
9th of January 2019, based on fictional raw data provided.

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

    def check(self, models=[]):

        for m in models:
            if self.knowledge.location.id == m.knowledge.location.id and \
                    self.knowledge.area == m.knowledge.area:

                for c in m.knowledge.contacts:
                    if c not in self.knowledge.contacts:
                        continue

                self.message = m.message
                break
            else:
                continue

        print(self.message)
