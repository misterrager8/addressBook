import mysql.connector
from flask import Flask

from address_book import config

mysql_ = mysql.connector.connect(
    user=config.USER, password=config.PASSWORD, host=config.HOST
)
cursor_ = mysql_.cursor()

cursor_.execute("CREATE DATABASE IF NOT EXISTS AddressBook")
cursor_.execute(
    "CREATE TABLE IF NOT EXISTS AddressBook.contacts (id INT PRIMARY KEY AUTO_INCREMENT, first_name TEXT, mobile TEXT)"
)


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    with app.app_context():
        from address_book.views.contacts import contacts

        app.register_blueprint(contacts)

        return app
