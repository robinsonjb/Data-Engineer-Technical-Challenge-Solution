class Person:
    def __init__(self, nameid, first_name, last_name, birthdate, address, email, credit_card_type, credit_card_number):
        self.nameid = nameid
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.address = address
        self.email = email
        self.credit_card_type = credit_card_type
        self.credit_card_number = credit_card_number

    def personalinfo(self):
        print("ID: " + self.nameid)
        print("Name: " + self.first_name + " " + self.last_name)
        print("Birth date: " + self.birthdate)
        print("Home Address: " + self.address)
        print("Email Address: " + self.email)
        print("Credit Card Type: " + self.credit_card_type + ", Number: " + self.credit_card_number)