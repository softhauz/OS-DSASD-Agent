"""

Simultaneous Tracker: "Historian"

Date: July 11, 2020
Author: Karen Urate
File: model.py
Description: This file contains the class object representation for Knowledge.


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
class Knowledge:

    def __init__(self, location=None, contacts=[], area=""):
        self.id = 0
        self.location = location
        self.contacts = contacts
        self.area = area

    def print(self):
        print("Knowledge [" + str(self.id) + "]: " + str(self.location.text()) + " | Contacts: " + str(self.contacts) + " | Visited Area: " + self.area)