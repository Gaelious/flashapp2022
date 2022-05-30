class Contact():
    def __init__(self, name, number, date, genre):  

        self.name = name
        self.number = number
        self.date = date
        self.genre = genre

    def getName(self):
        return self.name

    def getNumber(self):
        return self.number

    def getAge(self):
        return self.date

    def getGenre(self):
        return self.genre

    def isAdult(self):
        year = self.date.split('-', 3)

        return int(year[0]) < 2004