class person:
    def __init__(self, personID, fname, lname, dob, email, number):
        self.personID = personID
        self.fname = fname
        self.lname = lname
        self.dob = dob
        self.email = email
        self.number = number

    def getPersonID(self):
        return self.personID

    def setFname(self, x):
        self.fname = x

    def getFname(self):
        return self.fname

    def setLname(self, x):
        self.lname = x

    def getLname(self):
        return self.lname

    def setDob(self, x):
        self.dob = x

    def getDob(self):
        return self.dob

    def setEmail(self, x):
        self.email = x

    def getEmail(self):
        return self.email

    def setNumber(self, x):
        self.number = x

    def getNumber(self):
        return self.number

    def toString(self):
        print(str(self.personID),
              self.fname,
              self.lname,
              self.dob,
              self.email,
              self.number)
