import logos.Person
import logos.kindness
import logos.love

import math

class God:
    Omnipotent = True
    Ubiquitous = True
    Omniscient = True
    Goodness = math.inf

@staticmethod
def GiveLife(name, birthDate):
    return logos.Person(name, birthDate)

staticmethod
def GiveGrace(person):
    if (not person._Grace):
        if (person.GodsWish.count() >= God.Goodness):
            return logos.Awake(person)