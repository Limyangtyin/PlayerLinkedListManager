class PLAYER:
    def __init__(self, uid, name):
        self.uid = uid
        self.name = name

    @property
    def uid(self):
        return self.uid

    @property
    def name(self):
        return self.name

    def __str__(self):
        return "I am Player"
