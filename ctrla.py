from model import *
import MySQLdb

class ctrla():
  def __init__(self):
    pass

  def addPerson(self, x):
    db = MySQLdb.connect("localhost","root","bre9ase4","contacts")
    cursor = db.cursor()
    sql = "INSERT INTO people (firstName, lastName, dob, emails, telNumbers) VALUES ('%s', '%s', '%s', '%s', '%s')" % (x.fname, x.lname, x.dob, x.emails, x.numbers)
    
    try:
      cursor.execute(sql)
      db.commit()
    except MySQLdb.Error, e:
      print(e)
      
    db.close()

  def deletePerson(self, personId):
    db = MySQLdb.connect("localhost","root","bre9ase4","contacts")
    cursor = db.cursor()
    sql = "DELETE FROM people WHERE personId = '%d'" % (personId)
    
    try:
      cursor.execute(sql)
      db.commit()
    except MySQLdb.Error, e:
      print(e)
      
    db.close()
    
  def viewPeople(self):
    db = MySQLdb.connect("localhost","root","bre9ase4","contacts")
    cursor = db.cursor()
    sql = "SELECT * FROM people"
    
    try:
      cursor.execute(sql)
      results = cursor.fetchall()
      for row in results:
        n = person(row[1],
                   row[2],
                   row[3],
                   row[4],
                   row[5])
        n.toString()
    except MySQLdb.Error, e:
      print(e)
      
    db.close()