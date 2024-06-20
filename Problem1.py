class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def change_owner(self, new_owner):
        self.owner = new_owner
        return self.owner


Vehicle1 = Vehicle('AAA123456', 'Car', 'Marky Mark')
print(Vehicle1.change_owner('Jake from State Farm'))

#Task2
class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participants = 0 

    def add_participant(self):
        self.participants += 1

    def get_participant_count(self):
        return self.participants