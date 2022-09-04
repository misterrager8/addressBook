from flask import current_app, render_template, request

from address_book.forms import AddContactForm
from address_book.models import Contact


@current_app.route("/")
def index():
    form = AddContactForm()
    return render_template("index.html", form=form, contacts_=Contact.all())
