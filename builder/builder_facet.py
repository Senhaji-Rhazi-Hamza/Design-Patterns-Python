class Person:
    def __init__(self):
        # address infos
        self.city = None
        self.country = None
        # professional infos
        self.company = None
        self.earns = None 
        # Personal infos
        self.name = None
        self.friends = []
        self.partner = None
    
    
    def __str__(self):
        return f"{self.name} lives in {self.city} in {self.country} earns {self.earns}" + \
            f"works in {self.works_in} has as a partner {self.partner} and have the following" + \
                f"friends {','.join(self.friends)}"
class PersonBuilder:
    
    def __init__(self, person=None):
        if person is None:
            self.person = Person()
        else : 
            self.person = person
    
    def build(self):
        return self.person

    @property
    def lives(self):
        return AdressPersonInfo(self.person)
    
    @property
    def works(self):
        return ProfessionalPersonInfo(self.person)
    
    @property
    def has(self):
        return PersonalPersonInfo(self.person)  
    

class AdressPersonInfo(PersonBuilder):
    
    def at(self, city):
        self.person.city = city
        return self
    
    def in_(self, country):
        self.person.country = country
        return self

class ProfessionalPersonInfo(PersonBuilder):
    
    def at(self, company):
        self.person.company = company
        return self
    
    def earns(self, earns):
        self.person.earns = earns
        return self

class PersonalPersonInfo(PersonBuilder):
    
    def as_partner(self, partner):
        self.person.partner = partner
        return self
    
    def as_friend(self, friend):
        self.person.friends.append(friend)
        return self


if __name__ == "__main__":
    pb = PersonBuilder()
    pb\
    .has\
        .as_friend('Hamza')\
        .as_friend('Othmane')\
        .as_partner('Sarah')\
    .lives\
        .at('Fez')\
        .in_('Morroco')\
    .works\
        .at('SFEIR')\
        .earns('Top secret')\
    .build()
    print(pb)

    