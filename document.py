"""
Simultaneous Tracker: "Historian"

Date: July 11, 2020
Author: Karen Urate
File: document.py
Description: This file demonstrates handling of user
inputs and encapsulating data into Tracker objects.

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

from agent import *

"""
TYPE 1: Handle user inputs for locations.
"""
input_location = "restaurant gym park 1 park home 5 home"
places = input_location.split()
visited = []
visit = Location()

for p in places:
    try:
        visit.id = int(p)
        visited.append(visit)
        visit = Location(0,[])
    except:
        visit.quarantines.append(p)
        continue

for v in visited:
    print("Location " + str(v.id) + ": " + str(v.quarantines))


"""
TYPE 2: Match locations.
"""
print("----------------------------------------------------------------")
print("Location to Match:")
matcher = Location(1,["office","gym","grocery store","house"])
matcher.print()
print("----------------------------------------------------------------")

found = False
for v in visited:
    if(v.match(matcher)):
        print("It's a match!")
        v.print()
        found = True
        break

if not found:
    print("Sorry, there is no match found.")
