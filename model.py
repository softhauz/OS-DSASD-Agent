class Model:

    def __init__(self, knowledge=None, message=""):
        self.id = 0
        self.knowledge = knowledge
        self.message = message

    def match(self, model=None):
        if (self.location.match(model.knowledge.location)) and \
            (any(self.knowledge.contacts == c for c in model.knowledge.contacts)) and \
            (self.knowledge.visit == model.knowledge.visit):
            return True

        return False

    def check(self, models=[]):

        for m in models:
            if self.knowledge.location.id == m.knowledge.location.id and \
                    self.knowledge.visit == m.knowledge.visit and \
                    self.knowledge.contacts == m.knowledge.contacts:
                self.message = m.message
                break
            else:
                continue

        print(self.message)
