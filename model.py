class person:
  def __init__(self, fname, lname, dob, emails, numbers):
    self.fname = fname
    self.lname = lname
    self.dob = dob
    self.emails = emails
    self.numbers = numbers
    
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
  
  def toString(self):
    print(self.fname,
          self.lname,
          self.dob,
          self.emails,
          self.numbers)
  
class number:
  def __init__(self, num, numType):
    self.num = num
    self.numType = numType
    
  def setNum(self, x):
    self.num = x
    
  def getNum(self):
    return self.num
    
  def setNumType(self, x):
    self.num = x
    
  def getNumType(self):
    return self.numType
  
class email:
  def __init__(self, email, numType):
    self.email = email
    self.emailType = emailType
    
  def setEmail(self, x):
    self.email = x
    
  def getEmail(self):
    return self.email
    
  def setEmailType(self, x):
    self.email = x
    
  def getEmailType(self):
    return self.emailType