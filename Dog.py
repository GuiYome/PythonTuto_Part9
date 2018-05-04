class Dog:

    kind = 'canine'         # class variable shared by all instances

    tricks = []

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

    def add_trick(self, trick):
        self.tricks.append(trick)
