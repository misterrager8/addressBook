import csv
import os
import sys

import MySQLdb

from model import *


class Ctrla:
    def __init__(self):
        pass

    @classmethod
    def run_query(cls, stmt):
        db = MySQLdb.connect("localhost", "root", "bre9ase4", "contacts")
        cursor = db.cursor()

        try:
            cursor.execute(stmt)
            db.commit()
        except MySQLdb.Error, e:
            print(e)

        db.close()

    @classmethod
    def run_read_query(cls, stmt):
        db = MySQLdb.connect("localhost", "root", "bre9ase4", "contacts")
        cursor = db.cursor()

        try:
            cursor.execute(stmt)
            return cursor.fetchall()
        except MySQLdb.Error, e:
            print(e)

    @classmethod
    def run_search_query(cls, stmt, search_term):
        db = MySQLdb.connect("localhost", "root", "bre9ase4", "contacts")
        cursor = db.cursor()

        try:
            cursor.execute(stmt, ("%" + search_term + "%",))
            return cursor.fetchall()
        except MySQLdb.Error, e:
            print(e)

    def add_person(self, x):
        sql = "INSERT INTO people (firstName, lastName, dob, emails, telNumbers) VALUES ('%s', '%s', '%s', '%s', '%s')"\
              % (x.fname, x.lname, x.dob, x.email, x.number)
        self.run_query(sql)

    def delete_person(self, person_id):
        sql = "DELETE FROM people WHERE personId = '%d'" % person_id
        self.run_query(sql)

    def view_people(self):
        results = []
        sql = "SELECT * FROM people"
        for row in self.run_read_query(sql):
            n = Person(row[0], row[1], row[2], row[3], row[4], row[5])
            results.append(n)

        return results

    def edit_person(self, person_id, edit_id, edit):
        sql0 = "UPDATE people SET firstName = '%s' WHERE personId = '%d'" % (edit, person_id)
        sql1 = "UPDATE people SET lastName = '%s' WHERE personId = '%d'" % (edit, person_id)
        sql2 = "UPDATE people SET dob = '%s' WHERE personId = '%d'" % (edit, person_id)
        sql3 = "UPDATE people SET emails = '%s' WHERE personId = '%d'" % (edit, person_id)
        sql4 = "UPDATE people SET telNumbers = '%s' WHERE personId = '%d'" % (edit, person_id)

        if edit_id == 0:
            self.run_query(sql0)
        elif edit_id == 1:
            self.run_query(sql1)
        elif edit_id == 2:
            self.run_query(sql2)
        elif edit_id == 3:
            self.run_query(sql3)
        elif edit_id == 4:
            self.run_query(sql4)

    def search_person(self, search_id, search_term):
        people_list = []
        b = {}
        sql0 = "SELECT * FROM people WHERE firstName LIKE %s"
        sql1 = "SELECT * FROM people WHERE lastName LIKE %s"
        sql2 = "SELECT * FROM people WHERE dob LIKE %s"
        sql3 = "SELECT * FROM people WHERE emails LIKE %s"
        sql4 = "SELECT * FROM people WHERE telNumbers LIKE %s"

        if int(search_id) == 0:
            b = self.run_search_query(sql0, search_term)
        elif int(search_id) == 1:
            b = self.run_search_query(sql1, search_term)
        elif int(search_id) == 2:
            b = self.run_search_query(sql2, search_term)
        elif int(search_id) == 3:
            b = self.run_search_query(sql3, search_term)
        elif int(search_id) == 4:
            b = self.run_search_query(sql4, search_term)

        for row in b:
            x = Person(row[0], row[1], row[2], row[3], row[4], row[5])
            people_list.append(x)

        return people_list

    def import_people(self):
        imported = []
        csv_data = csv.reader(file("input.csv"))
        for row in csv_data:
            q_person = Person(None, row[0], row[1], row[2], row[3], row[4])
            imported.append(q_person)

        print(str(len(imported)) + " person(s) found.")
        for item in imported:
            item.to_string()

        answer = raw_input("Add these people? ")
        if answer == "Y" or answer == "y":
            for item in imported:
                self.add_person(item)

    def export_people(self):
        sql = "SELECT * FROM people"
        results = self.run_read_query(sql)

        with open("output.csv", "w") as f:
            a = csv.writer(f, delimiter=",")
            a.writerow(["Person ID", "First Name", "Last Name", "DOB", "Email", "Number"])
            a.writerows(results)

    def gui_view_people(self):
        results = []
        for submission in self.view_people():
            results.append([submission.personID,
                            submission.fname,
                            submission.lname,
                            submission.dob,
                            submission.email])

        with open("peopleList.csv", "wb") as f:
            writer = csv.writer(f)
            writer.writerows(results)

    def gui_add_person(self):
        csv_data = csv.reader(file("temp.csv"))
        for row in csv_data:
            sql = "INSERT INTO people (firstname, lastname, dob, emails, telNumbers) VALUES ('%s', '%s', '%s', " \
                  "'%s', '%s')" % (
                      row[1], row[2], row[3], row[4], row[5])
            self.run_query(sql)

        os.remove("temp.csv")
        self.gui_view_people()

    def gui_del_person(self, person_id):
        pass

    def gui_search_person(self, search_id, search_term):
        pass

    def gui_edit_person(self, person_id, edit_id, edit):
        pass


if __name__ == "__main__":
    if sys.argv[1] == "add":
        Ctrla().gui_add_person()