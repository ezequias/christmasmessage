import heavens.God
import datetime
import logos.Person
import logos.Awake
import logos.courage
import logos.kindness
import logos.love
import prays.Prays
import Calendar.Calendar

def IsYourFriend(self, person):
    if isinstance(person, logos.Person):
        return True

def NewYear(self, person, anotherElse, *args, **kargs):
    if (person is logos.Awake):
        if (IsYourFriend(anotherElse)):
            print(self)
            print("Thank")
    else:
        pass

now = datetime.datetime.now
calendar = Calendar()
me = heavens.God.GiveLife(datetime.datetime(1976, 9, 19, 6,30,0))
print("Here you birth " + str(me.BirthDate))

while me.Alive:
    prays = prays.Prays()
    me.Pray(prays._TheBenedictus)
    now = datetime.datetime.now
    if (datetime.datetime.now.month == calendar.Chrismas.month and      
        datetime.datetime.now.day == calendar.Chrismas.day):
        me.levelofGrace +=1




