# ---------------------------------------------------
# -- Databases => SQLite => Training On Everything --
# ---------------------------------------------------

import sqlite3

def get_all_data():

  try:

    # Connect To Database
    db = sqlite3.connect("order food app.db")

    # Print Success Message
    print("Connected To Database Successfully")
    
    # Setting Up The Cursor
    cr = db.cursor()
    
    # Create The Tables and Fields
    cr.execute(
        "create table if not exists skills (name text, progress integer, user_id integer)")
    cr.execute(
         "create table if not exists users (user_id integer, name text, country text, birthday integer, phone_number integer)")
    
    
    # Loop to adding data
    my_list = ["Mahmoud", "Mina", "Moaaz", "Mostafa", "Moutaz", "Farida", "Tian"]

    for key, user in enumerate(my_list):

        cr.execute(f"insert into users(user_id, name) values({key + 1}, '{user}')")
        
    # Update Data
    # cr.execute("UPDATE users set name = 'Xia' WHERE user_id = 7 ")
    # # cr.execute("update users set name = 'Mahmoud' where user_id = 1")

    # Delete Data
    # cr.execute("delete from users where user_id = 4")

    # Fetch Data From Database
    cr.execute("select * from users")

    # Assign Data To Variable Get all data Fetch data
    results = cr.fetchall()

    # Print Number Of Rows
    print(f"Database Has {len(results)} Rows.")

    # Printing Message
    print("Showing Data:")

    # Loop On Results
    for row in results:

      print(f"UserID => {row[0]},", end=" ")

      print(f"Username => {row[1]}")

  except sqlite3.Error as er:

    print(f"Error Reading Data {er}")

  finally:

    if (db):

      # Close Database Connection
      db.close()

      print("Connection To Database Is Closed")

get_all_data()