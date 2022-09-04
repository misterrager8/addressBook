from address_book import cursor_, mysql_


class Contact:
    def __init__(self, first_name: str, mobile: str, id: int = None):
        self.first_name = first_name
        self.mobile = mobile
        self.id = id

    def insert(self):
        cursor_.execute(
            "INSERT INTO AddressBook.contacts (first_name, mobile) VALUES (%s, %s)",
            (self.first_name, self.mobile),
        )
        mysql_.commit()

    @classmethod
    def all(cls):
        cursor_.execute("SELECT first_name, mobile, id FROM AddressBook.contacts")
        results = cursor_.fetchall()
        return [Contact(i[0], i[1], i[2]) for i in results]

    @classmethod
    def get(cls, id: int):
        cursor_.execute(
            "SELECT first_name, mobile, id FROM AddressBook.contacts WHERE id=%s", (id,)
        )
        result = cursor_.fetchone()
        return Contact(result[0], result[1], result[2])

    def delete(self):
        cursor_.execute("DELETE FROM AddressBook.contacts WHERE id=%s", (self.id,))
        mysql_.commit()
