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
        referral = input(self.greeting)
        individual = Individual(referral)
        points = input(str(individual.name) + ", please tell me about all of the places that you've been to\n"
                                     "  on 9th of January 2019, starting with the most recent.\n"
                                     " For example, if you went to the gym at Location 1 and ate at a restaurant\n"
                                     " at Location 4, you can simply type, 'gym 1 restaurant 4'.\n")



class Individual:
    def __init__(self,name):
        self.id = 0
        self.name = name
        self.locations = []
        self.contacts = []

class Location:
    def __init__(self,id,quarantines):
        self.id = id
        self.quarantines = quarantines

class Model:
    def __init__(self,knowledge):
        self.id = 0
        self.knowledge = knowledge

    def match(self, model):
        base = model.knowledge.base

        for i in base:
            if i not in self.knowledge.base:
                return False

        return True

class Knowledge:
    def __init__(self,base):
        self.id = 0
        self.base = base

    def process(self, information):
        return None