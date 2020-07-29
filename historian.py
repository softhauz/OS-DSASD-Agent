from agent import *

"""
Simultaneous Tracker: "Historian"

Date: July 11, 2020
Author: Karen Urate
File: historian.py
Description: This file is the main runner for Simultaneous Tracker:
Historian.  

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

def main():

    greeting = " I will be your knowledge-based agent for today.\n" \
               " I am powered by an artificial intelligence that will help you find out\n" \
               " if you have contracted the Covid-19 disease on January 9, 2020\n" \
               " based on the information that I have. I will also be able to\n" \
               " tell you about the source of infection and how you've contracted Covid-19,\n" \
               " if you've been infected. My creator is a Software Developer named Karen Urate.\n"\
               " The start of my development began on July 11, 2020. I was born on the next day.\n"\
               " I'm continuously learning, so I might be able to give you better results as you tell me more\n" \
               " about how your day went on 9th of January 2020. Let's get started.\n" \
               " What name would you prefer to be called?\n"

    agent = Agent(greeting,"Karen Bot")
    agent.greet()
    agent.process()

if __name__ == "__main__":
    main()