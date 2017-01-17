class Student(Person):
    def __init__(self, fName, lName, idN, arr):
        Person.__init__(self, fName, lName, idN)
        self.scores = arr
    def calculate(self):
        avg = 0
        length = len(self.scores)
        for i in range(length):
            avg += self.scores[i]
        avg = avg/length
        if avg>= 90:
            return "O"
        if avg>= 80:
            return "E"
        if avg >= 70:
            return "A"
        if avg>= 55:
            return "P"
        if avg>=40:
            return "D"
        else:
            return "T"
