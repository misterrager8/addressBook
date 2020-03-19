from model import *
import MySQLdb

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