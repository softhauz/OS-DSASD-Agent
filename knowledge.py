class Knowledge:

    def __init__(self, location=None, contacts=[], visit=""):
        self.id = 0
        self.location = location
        self.contacts = contacts
        self.visit = visit

    def print(self):
        print("Knowledge: " + str(self.location.text()) + " " + str(self.contacts) + " " + self.visit)