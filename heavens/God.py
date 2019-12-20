import logos.Person
import life
import sys

class God:
    Omnipotent = True
    Ubiquitous = True
    Omniscient = True
    Goodness = sys.maxsize

@staticmethod
def GiveLife(name, birthDate):
    return logos.Person(name, birthDate)

staticmethod
def GiveGrace(person):
    if (not person._Grace):
        if (person.GodsWish.count() >= God.Goodness):
            return life.Awake(person)