from model import *
import MySQLdb
import csv

class ctrla():
  def __init__(self):
    pass
  
  def runQuery(self, stmt):
    db = MySQLdb.connect("localhost","root","bre9ase4","contacts")
    cursor = db.cursor()
    
    try:
      cursor.execute(stmt)
      db.commit()
    except MySQLdb.Error, e:
      print(e)
      
    db.close()
    
  def runReadQuery(self, stmt):
    db = MySQLdb.connect("localhost","root","bre9ase4","contacts")
    cursor = db.cursor()
    
    try:
      cursor.execute(stmt)
      return cursor.fetchall()
    except MySQLdb.Error, e:
      print(e)
    
  def runSearchQuery(self, stmt, searchTerm):
    db = MySQLdb.connect("localhost","root","bre9ase4","contacts")
    cursor = db.cursor()
    
    try:
      cursor.execute(stmt, ("%" + searchTerm + "%",))
      return cursor.fetchall()
    except MySQLdb.Error, e:
      print(e)
    
  def addPerson(self, x):
    sql = "INSERT INTO people (firstName, lastName, dob, emails, telNumbers) VALUES ('%s', '%s', '%s', '%s', '%s')" % (x.fname, x.lname, x.dob, x.email, x.number)
    self.runQuery(sql)

  def deletePerson(self, personId):
    sql = "DELETE FROM people WHERE personId = '%d'" % (personId)
    self.runQuery(sql)
    
  def viewPeople(self):
    results = []
    sql = "SELECT * FROM people"
    for row in self.runReadQuery(sql):
      n = person(row[0], row[1], row[2], row[3], row[4], row[5])
      results.append(n)
      
    return results
  
  def editPerson(self, ID, editID, edit):
    sql0 = "UPDATE people SET firstName = '%s' WHERE personId = '%d'" % (edit, ID)
    sql1 = "UPDATE people SET lastName = '%s' WHERE personId = '%d'" % (edit, ID)
    sql2 = "UPDATE people SET dob = '%s' WHERE personId = '%d'" % (edit, ID)
    sql3 = "UPDATE people SET emails = '%s' WHERE personId = '%d'" % (edit, ID)
    sql4 = "UPDATE people SET telNumbers = '%s' WHERE personId = '%d'" % (edit, ID)
    
    if editID == 0:
      self.runQuery(sql0)
    elif editID == 1:
      self.runQuery(sql1)
    elif editID == 2:
      self.runQuery(sql2)
    elif editID == 3:
      self.runQuery(sql3)
    elif editID == 4:
      self.runQuery(sql4)
      
  def searchPerson(self, searchID, searchTerm):
    peopleList = []
    b = {}
    sql0 = "SELECT * FROM people WHERE firstName LIKE %s"
    sql1 = "SELECT * FROM people WHERE lastName LIKE %s"
    sql2 = "SELECT * FROM people WHERE dob LIKE %s"
    sql3 = "SELECT * FROM people WHERE emails LIKE %s"
    sql4 = "SELECT * FROM people WHERE telNumbers LIKE %s"

    if int(searchID) == 0:
      b = self.runSearchQuery(sql0, searchTerm)
    elif int(searchID) == 1:
      b = self.runSearchQuery(sql1, searchTerm)
    elif int(searchID) == 2:
      b = self.runSearchQuery(sql2, searchTerm)
    elif int(searchID) == 3:
      b = self.runSearchQuery(sql3, searchTerm)

    for row in b:
      x = person(row[0], row[1], row[2], row[3], row[4], row[5])
      peopleList.append(x)

    return peopleList
  
  def importPeople(self):
    imported = []
    csv_data = csv.reader(file("input.csv"))
    for row in csv_data:
      qPerson = person(None, row[0], row[1], row[2], row[3], row[4])
      imported.append(qPerson)
      
    print(str(len(imported)) + " person(s) found.")
    for item in imported:
      item.toString()
      
    answer = raw_input("Add these people? ")
    if answer == "Y" or answer == "y":
      for item in imported:
        self.addPerson(item)
        
  def exportPeople(self):
    sql = "SELECT * FROM people"
    results = self.runReadQuery(sql)

    with open("output.csv", "w") as f:
      a = csv.writer(f, delimiter = ",")
      a.writerow(["Person ID", "First Name", "Last Name", "DOB", "Email", "Number"])
      a.writerows(results)