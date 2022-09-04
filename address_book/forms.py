from wtforms import Form, StringField


class AddContactForm(Form):
    first_name = StringField("First Name")
    mobile = StringField("Mobile")
