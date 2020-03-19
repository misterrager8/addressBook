import sys
from ctrla import *
from model import *

options = ["View All","Add","Delete","Edit","Search","Import","Export","Exit"]
ac = ctrla()

class mainMenu():
  def __init__(self):
    while True:
      self.printPeople()
      self.listOptions(options)
      userChoice = input("What would you like to do? ")
      
      if options[userChoice] == "View All":
        self.printPeople()
      elif options[userChoice] == "Add":
        fname = raw_input("First Name: ")
        lname = raw_input("Last Name: ")
        dob = raw_input("Date of Birth: ")
        email = raw_input("Email: ")
        number = raw_input("Number: ")
        
        x = person(None, fname, lname, dob, email, number)
        ac.addPerson(x)
      elif options[userChoice] == "Delete":
        whichOne = input("Which one? ")
        ac.deletePerson(whichOne)
      elif options[userChoice] == "Edit":
        print("temp4")
      elif options[userChoice] == "Search":
        print("temp5")
      elif options[userChoice] == "Import":
        print("temp6")
      elif options[userChoice] == "Export":
        print("temp7")
      elif options[userChoice] == "Exit":
        sys.exit()
    
  def listOptions(self, listX):
    for idx, i in enumerate(listX):
      print(str(idx) + " - " + i)
      
  def printPeople(self):
    for i in ac.viewPeople():
      i.toString()