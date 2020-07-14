"""
Tracker

Date: July 11, 2020
Author: Karen Urate
File: agent.py
Description: This file contains the Location class object.

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