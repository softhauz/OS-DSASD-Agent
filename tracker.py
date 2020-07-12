from agent import *

"""
Tracker

Date: July 11, 2020
Author: Karen Urate
------------------------------------------------------------------
                            DESCRIPTION
------------------------------------------------------------------
Create a knowledge-based agent that will compute and trace
the source of infection for an individual who has contracted Covid-19
disease from Location 1 to Location 6 in a span of 12-hour period on
9th of January 2019, based on fictional raw data provided.

The agent must have an ability to learn, create new models,
and find the source of infection based on built-up knowledge base.
"""
CATEGORY_LOCATION = 0
CATEGORY_CONTACT = 1

QUARANTINES = [
    Location(1,["office","gym","grocery store"]),
    Location(2,["home","park","beach","mall"]),
    Location(3,["home","park","beach","mall"]),
    Location(4,["restaurant"]),
    Location(5,["home","park","beach","mall"]),
    Location(6,["campground"])
]

def main():

    greeting = "Hi! I will be your agent for today. I'm here to help you find out\n" \
               " if you have contracted the Covid-19 disease on January 9, 2019\n" \
               " based on the information that I have. I will also be able to\n" \
               " tell you about the source of infection and how you contracted Covid-19,\n" \
               " if you've been infected. I'm continuously learning,\n" \
               " so I might be able to give you better results as you tell me more\n" \
               " about the situation. Let's get started. What name would you prefer\n" \
               " to be called?"

    agent = Agent(greeting,"Karen")
    agent.interrogate()

if __name__ == "__main__":
    main()