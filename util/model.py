class Person:
    def __init__(self, person_id, fname, lname, dob, email, number):
        self.personID = person_id
        self.fname = fname
        self.lname = lname
        self.dob = dob
        self.email = email
        self.number = number

    def get_person_id(self):
        return self.personID

    def set_fname(self, x):
        self.fname = x

    def get_fname(self):
        return self.fname

    def set_lname(self, x):
        self.lname = x

    def get_lname(self):
        return self.lname

    def set_dob(self, x):
        self.dob = x

    def get_dob(self):
        return self.dob

    def set_email(self, x):
        self.email = x

    def get_email(self):
        return self.email

    def set_number(self, x):
        self.number = x

    def get_number(self):
        return self.number

    def to_string(self):
        print(str(self.personID),
              self.fname,
              self.lname,
              self.dob,
              self.email,
              self.number)
