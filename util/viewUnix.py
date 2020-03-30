import sys
from ctrla import *
from model import *

options = ["View All","Add","Delete","Edit","Search","Import","Export","Exit"]
attribs = ["First Name", "Last Name", "Date of Birth", "Email", "Number"]
ac = ctrla()

class mainMenu():
  def __init__(self):
    while True:
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
        whichOne = input("Which one? ")
        self.listOptions(attribs)
        editType = input("Edit Type? ")
        edit = raw_input("Enter change: ")
        ac.editPerson(whichOne, editType, edit)
      elif options[userChoice] == "Search":
        self.listOptions(attribs)
        searchID = input("Search By? ")
        searchTerm = raw_input("Search term? ")
        searchResults = ac.searchPerson(searchID, searchTerm)
        
        print(str(len(searchResults)) + " record(s) found.")
        for i in searchResults:
          i.toString()
      elif options[userChoice] == "Import":
        ac.importPeople()
      elif options[userChoice] == "Export":
        ac.exportPeople()
      elif options[userChoice] == "Exit":
        sys.exit()
    
  def listOptions(self, listX):
    for idx, i in enumerate(listX):
      print(str(idx) + " - " + i)
      
  def printPeople(self):
    for i in ac.viewPeople():
      i.toString()