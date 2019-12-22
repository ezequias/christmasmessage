class Person:    
    _Nome = None
    class Inner:
        Inspiration = "God"
        MessageEducation1 = None
        MessageEducation2 = None
        MessageEducationPF = None
        MessageEducationObg = None
    BirthDate = None
    _Ego = None
    _Alive = None
    _Alert = None
    _Polite = None
    _Awake = None
    _Friends = None
    _Awake = None

    goodwords = ('love', 'God', 'Christ', 'peace', 'charity' )

    def __init__(self, name, birthDate):
        self.Nome = name
        self.BirthDate = birthDate
        self._Alive = True
        self.MessageEducation1 = "Good morning!"
        self.MessageEducation2 = "Good evening!"
        self.MessageEducation3 = "Good night"
        self.MessageEducationOffer = "Do you need something?"
        self.MessageEducationPF = "Please"
        self.MessageEducationObg = "Thank you"
        self.Alert = True
        self.Polite = True


    # region Important Behaviours
    def Pray(self, message, levelOfGrace):
        if (ThereIsGoodWords(message)):
            levelOfGrace += 1

    def ThereIsGoodWords(self, message, levelOfGrace):
        return message in goodwords


    # endregion