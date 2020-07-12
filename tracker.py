from agent import *
from probes import *

"""
Tracker

Date: July 11, 2020
Author: Karen Urate
File: tracker.py
Description: This file is the main runner for Tracker.  

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

QUARANTINES = [
    Location(1,["office","gym","grocery store","house"]),
    Location(2,["home"]),
    Location(3,["home"]),
    Location(4,["restaurant"]),
    Location(5,["park","beach","mall"]),
    Location(6,["campground"])
]

CONTACTS = ["AA","BA","CA","DA","EA","FA","GA","HA","IA","JG","AB","BB","CB","EB","Couple 1","Couple 2","Couple 3","Relatives","Six Friends","Locals","Socials"]

MODEL_1 = Model(
    Knowledge(
        QUARANTINES[0],
        ["AA","BA","CA"],
        "office"
    ))

MODEL_2 = Model(
    Knowledge(
        QUARANTINES[0],
        ["AA"],
        "office"
    ))

MODEL_3 = Model(
    Knowledge(
        QUARANTINES[0],
        ["BA"],
        "office"
    ))

MODEL_4 = Model(
    Knowledge(
        QUARANTINES[0],
        ["CA"],
        "office"
    ))

MODEL_5 = Model(
    Knowledge(
        QUARANTINES[0],
        ["EA"],
        "grocery store"
    ))

MODEL_6 = Model(
    Knowledge(
        QUARANTINES[0],
        ["BA"],
        "house"
    ))

MODEL_7 = Model(
    Knowledge(
        QUARANTINES[0],
        ["CA"],
        "house"
    ))

MODEL_8 = Model(
    Knowledge(
        QUARANTINES[0],
        ["BA","CA"],
        "house"
    ))

MODEL_9 = Model(
    Knowledge(
        QUARANTINES[0],
        ["DA"],
        "gym"
    ))

MODEL_10 = Model(
    Knowledge(
        QUARANTINES[5],
        ["six friends"],
        "campground"
    ))

MODEL_11 = Model(
    Knowledge(
        QUARANTINES[5],
        ["CB"],
        "campground"
    ))

MODEL_12 = Model(
    Knowledge(
        QUARANTINES[5],
        ["EB"],
        "campground"
    ))


MODEL_13 = Model(
    Knowledge(
        QUARANTINES[5],
        ["CB","EB"],
        "campground"
    ))

MODEL_14 = Model(
    Knowledge(
        QUARANTINES[1],
        ["AB"],
        "home"
    ))

MODEL_15 = Model(
    Knowledge(
        QUARANTINES[1],
        ["BB"],
        "home"
    ))

MODEL_16 = Model(
    Knowledge(
        QUARANTINES[1],
        ["AB","BB"],
        "home"
    ))

MODEL_17 = Model(
    Knowledge(
        QUARANTINES[2],
        ["AB"],
        "home"
    ))

MODEL_18 = Model(
    Knowledge(
        QUARANTINES[2],
        ["BB"],
        "home"
    ))

MODEL_19 = Model(
    Knowledge(
        QUARANTINES[2],
        ["AB","BB"],
        "home"
    ))

MODEL_20 = Model(
    Knowledge(
        QUARANTINES[3],
        ["CB"],
        "restaurant"
    ))

MODEL_21 = Model(
    Knowledge(
        QUARANTINES[3],
        ["EB"],
        "restaurant"
    ))

MODEL_22 = Model(
    Knowledge(
        QUARANTINES[3],
        ["CB","EB"],
        "restaurant"
    ))

def main():

    greeting = "Hi, I'm Karen Bot! I will be your knowledge-based agent for today.\n" \
               " I am powered by an artificial intelligence that will help you find out\n" \
               " if you have contracted the Covid-19 disease on January 9, 2020\n" \
               " based on the information that I have. I will also be able to\n" \
               " tell you about the source of infection and how you've contracted Covid-19,\n" \
               " if you've been infected. My creator is a Software Developer named Karen Urate.\n"\
               " The start of my development began on July 11, 2020. I was born on the next day.\n"\
               " I'm continuously learning, so I might be able to give you better results as you tell me more\n" \
               " about how your day went on 9th of January 2020. Let's get started.\n" \
               " What name would you prefer to be called?\n"

    locations = []
    data = None
    state = 0

    agent = Agent(greeting,"Karen")
    agent.greet()

    # start with location
    data = agent.interrogate(M001)
    state = agent.process(TYPE_LOCATION,data)
    original = data
    loc_filter = agent.find(TYPE_LOCATION,original)

    # find valid location
    if state == ERR_LOCATION_NOT_INDICATED:
        data = agent.interrogate(M002)
        state = agent.process(TYPE_LOCATION,data)
        i = 0

        if state == ERR_LOCATION_NOT_INDICATED:
            agent.reply(M003)
            agent.reply(M012)
            agent.reply(original)

        while (state == ERR_LOCATION_NOT_INDICATED) and (i < len(loc_filter)):
            answer = agent.interrogate(loc_filter[i])

            if answer.strip().lower() in AFFIRMATIONS:
                data = str(agent.find(TYPE_RESPONSE_LOCATION,loc_filter[i]))

            state = agent.process(TYPE_LOCATION,data)
            i = i + 1

        if state == ERR_LOCATION_NOT_INDICATED:
            agent.reply(M009)
            exit
        elif state == ERR_NOT_COMPROMISED:
            agent.reply(M010)
        else:
            agent.reply(M011)
            # find a matching location


if __name__ == "__main__":
    main()