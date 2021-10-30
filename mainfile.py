import csv
import psycopg2
from Person import Person

persons = []
# Opening csv file
csvfile = open("MOCK_DATA.csv", 'r')
# creating a csv reader object
csvreader = list(csv.reader(csvfile))
# Removes header row
csvreader = csvreader[1:]

# extracting each data row one by one and appends object to persons list
for i in csvreader:
    p = Person(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7])
    persons.append(p)

# Database information
db_host = ""
db_name = ""
db_user = ""
db_pass = ""
port = ""

# connect to the db
try:
    con = psycopg2.connect(host = db_host,database = db_name, user = db_user,password = db_pass,port=port)
    print("Succesfully connected to Database")
    # cursor
    cur = con.cursor()

    # Requesting user input for card type
    cardtype = input("Enter a card type (Enter exit to stop): ")


    while cardtype != "exit":
        # execute query
        cur.execute("SELECT * FROM clean WHERE credit_card_type = '" + cardtype + "' ORDER BY birth_date")
        rows = cur.fetchall()

        # allows user to re-enter a card type if none matches the query
        # fetchall() returns an empty list if is no record matches the query criteria
        if rows == []:
            print("No person in this database has this card type")
            print()
            cardtype = input("Enter a card type (Enter exit to stop): ")
        else:
            # returns all the results from the query if it returns a value
            for r in rows:
                z = r[7]
                print("{" + r[1] + " " + r[2] + "}, born {" + r[3].strftime("%m/%d/%Y") + "}")
                print("Has a/an {" + r[6] + "} credit card ending in {" + z[-4:] + "}")
                print("Contact this person by email at: {" + r[4] + "}")
                print("Or by mail at {" + r[5] + "}")
                print()

            cardtype = input("Enter a card type (Enter exit to stop): ")

    # closing the cursor
    cur.close()

    # close connection to db
    con.close()

except ConnectionError:
    print("Failed to connect to database")
finally:
    print("Disconnected From Database")
