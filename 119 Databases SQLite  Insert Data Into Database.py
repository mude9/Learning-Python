# ------------------------------------------------------
# -- Databases => SQLite => Insert Data Into Database --
# ------------------------------------------------------
# - cursor => All Operation in SQL Done By Cursor Not The Connection Itself
# - commit => Save All Changes
# ------------------------------------------------------

# Import SQLite Module
import sqlite3

# Create Database And Connect
db = sqlite3.connect("Order Food app.db")

# Setting Up The Cursor
cr = db.cursor()

# Create The Tables and Fields
cr.execute(
    "create table if not exists skills (name text, progress integer, user_id integer)")
cr.execute(
    "create table if not exists users (user_id integer, name text, country text, birthday integer, phone_number integer)")

# Inserting Data
# cr.execute("insert into users(user_id, name, country) values(1, 'Mahmoud', 'Egypt')")
# cr.execute("insert into users(user_id, name, country) values(2, 'Mina', 'Yeman')")
# cr.execute("insert into users(user_id, name, country) values(3, 'Moaaz', 'Egypt')")

# my_list = ["Mahmoud", "Mina", "Moaaz", "Mostafa", "Moutaz", "Farida"]
# country_list = ["Egypt", "China", "Yeman", "Zampia", "China", "Yeman"]

# for key, user, name, country in enumerate(my_list, country_list):
#     cr.execute(f"insert into users(user_id, name, country) values({key + 1}, '{user}', {country})")
    
my_list = ["Mahmoud", "Mina", "Moaaz", "Mostafa", "Moutaz", "Farida"]
country_list = ["Egypt", "China", "Yemen", "Zambia", "China", "Yemen"]

for key, (user, country) in enumerate(zip(my_list, country_list), start=1):
    cr.execute(f"INSERT INTO users(user_id, name, country) VALUES({key}, '{user}', '{country}')")



# for name, country in enumerate(country_list):
#     cr.execute(f"insert into users(name, country) values({name}, )")
    

# Save (Commit) Changes
db.commit()

# Close Database
db.close()