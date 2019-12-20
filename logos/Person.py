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

    def __init__(self, name, birthDate):
        self.Nome = name
        self.BirthDate = birthDate
        self._Alive = True
        self.MessageEducation1 = "Olá Bom dia!"
        self.MessageEducation2 = "Precisa de alguma coisa?"
        self.MessageEducationPF = "Por favor"
        self.MessageEducationObg = "Obrigado"
        self.Alert = True
        self.Polite = True


# region Important Behaviours
    def Awake(self, *args):
        pass
# endregion