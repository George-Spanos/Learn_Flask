
class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

        def __getitem__(self):
            return self

    def initials(self):
        return "{},{}.".format(self.firstname[0], self.lastname[1])
