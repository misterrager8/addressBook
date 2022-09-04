from flask import Blueprint, redirect, render_template, request

from address_book.forms import AddContactForm
from address_book.models import Contact

contacts = Blueprint("contacts", __name__)


@contacts.route("/add_contact", methods=["POST"])
def add_contact():
    form = AddContactForm(request.form)

    contact_ = Contact(form.first_name.data, form.mobile.data)
    contact_.insert()

    return redirect(request.referrer)


@contacts.route("/edit_contact", methods=["POST"])
def edit_contact():
    contact_ = Contact.get(int(request.args.get("id_")))

    return redirect(request.referrer)


@contacts.route("/delete_contact")
def delete_contact():
    contact_ = Contact.get(int(request.args.get("id_")))
    contact_.delete()

    return redirect(request.referrer)
