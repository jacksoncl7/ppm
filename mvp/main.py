import sqlite3
from datetime import date

def main():
    option = int(input("password manager:\n
                       \tpress 1 to include new passwords\n
                       \tpress 2 to query a password\n")
    if option == 1:
        insert('./databases/password.db')
    elif option == 2:
        select('./databases/password.db')
    else:
        print("Option Error, option " + option +" is not implemented")

# TODO: abstract for class
def insert(db_path):
    db_connection = open_connection(db_path)
    #inputs
    email = text_value_input("email")
    service = text_value_input("service")
    secret = text_value_input("secret")
    url_service = text_value_input("url service")
    date = date.today().strftime("%d/%m/%y")

    insert_str = create_string_insert(email, service, secret, url_service, date)
    db_connection

def create_string_insert(email, service, secret, url_service, date):
    string = "INSERT INTO secrets VALUES "
    tuple_values = (email, service, secret, url_service, date)
    string += str(tuple_values)

# TODO: abstract for class
def select_all(db_path):
    db_connection = open_connection(db_path)

def open_connection(db_path):
    return sqlite3.connect(db_path)

def close_connection(database_connection)
    database_connection.close()

def text_value_input(label):
    text = input_text_label(label)
    rectification = retification_text_input(label, text)

def input_text_label(label)
    return str(input("input your new content to " + label))

def retification_text_input(label, text):
    rectification = 0
    while (retification != 1):
        rectification = int(input("The " + label + "content inputted was "+ text +":\n
                                   \tpress 1 to confirm your inputted content\n
                                   \tpress 2 to input a new content to" + label + "\n"))
        if retification == 2:
            text = input_text_label(label)
    return text

if name == "__main__":
    main()
