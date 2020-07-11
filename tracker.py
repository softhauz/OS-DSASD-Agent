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
class Agent():
    def __init__(self, greeting, name):
        self.id = "A00"
        self.greeting = greeting
        self.name = name
        self.models = []
        self.library = []

    def collect(self,information):
        self.library.append(information)

    def find(self):
        return None

    def learn(self):
        return None

    def interrogate(self):
        individual = Individual(self.greeting)

        individual.locations = input("Tell me about all of the places you've been to on 9th of January 2019,"
                                     " starting with the most recent."
                                     " For example, if you went to the gym at Location 1 and ate at a restaurant"
                                     " at Location 4, you can simply type, 'gym 1 restaurant 4'.")
                                     
        return None

class Individual:
    def __init__(self,name):
        self.id = 0
        self.name = name
        self.locations = []
        self.contacts = []

class Model:
    def __init__(self):
        self.id = 0
        self.knowledge = Knowledge()

    def match(self, model):
        return None

class Knowledge:
  def __init__(self,type):
    self.id = 0
    self.type = type
    self.base = []

def main():

    greeting = "Hi! I will be your agent for today. I'm here to help you find out" \
               " if you have contracted the Covid-19 disease on January 9, 2019" \
               " based on the information that I have. I will also be able to" \
               " tell you about the source of infection and how you contracted Covid-19," \
               " if you've been infected. I'm continuously learning," \
               " so I might be able to give you better results as you tell me more" \
               " about your situation. Let's get started. What name would you prefer" \
               " to be called?"

    agent = Agent(greeting,"Karen")

if __name__ == "__main__":
    main()