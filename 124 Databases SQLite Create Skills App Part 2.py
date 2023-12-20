# -----------------------------------------------------
# -- Databases => SQLite => Create Skills App Part 2 --
# -----------------------------------------------------

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


# Commit and Close Method
def commit_and_close():
  db.commit() # Save (Commit) Changes
  db.close()  # Close Database
  print("Connection To Database Is Closed")

# User ID
uid = input("please write your ID: ")

# Input Big Message
input_message = """
What Do You Want To Do ?
"s" => Show All Skills
"a" => Add New Skill
"d" => Delete A Skill
"u" => Update Skill Progress
"q" => Quit The App
"an" => Add name
"dn" => Delete Name
"ac" => Add Country

Choose Option:
"""

# Input Option Choose
user_input = input(input_message).strip().lower()

# Command List
commands_list = ["s", "a", "d", "u", "q", "an", "dn", "ac"]

"""Let's start adding our data in the SQL database"""

# Adding and Deleting Name
def add_name():
    
    user_name = input("Add user name: ").strip().title()
    add_country = input("Please add the country: ").strip().title()
    add_phone_number = input("Please add the phone nub: ").strip()
    cr.execute(
      f"insert into users(name, Country, user_id, phone_number) values('{user_name}', '{add_country}', '{uid}', '{add_phone_number}')")
          
    commit_and_close()

def delete_name ():
    
    del_name = input("Please write the name you want to delete: ").strip().title()
    cr.execute(f"DELETE from users(name, user_id) values('{del_name}'")
    
    commit_and_close()
   
# Showing skills

def show_skills():

  cr.execute(f"select * from skills where user_id = '{uid}'")

  results = cr.fetchall() 

  print(f"You Have {len(results)} Skills.")

  if len(results) > 0:

    print("Showing Skills With Progress: ")

  for row in results:

    print(f"Skill => {row[0]},", end=" ")

    print(f"Progress => {row[1]}%")

  commit_and_close()
  
  
# Adding skills

def add_skill():
    
    sk = input("Write Skill Name: ").strip().capitalize()
    choose_user_id = input("Please choose which user do you want to add the skill to: ")


    cr.execute(f"select name from skills where name = '{sk}' and user_id = '{choose_user_id}'")

    results = cr.fetchone()

    if results == None:  # Theres No Skill With This Name In Database
      
      prog = input("Write Skill Progress: ").strip()
      # choose_user_id = input("Please choose which user do you want to add the new skill to: ")
      cr.execute(f"insert into skills(name, progress, user_id) values('{sk}', '{prog}', '{choose_user_id}')")

        
    else:  # Theres A Skill With This Name in Database

         print("You Cannot Add It, Theres A Skill With This Name in Database")

    commit_and_close()
    

def delete_skill():

  sk = input("Write Skill Name: ").strip().capitalize()
  choose_user_id = input("Please choose which user do you want to delete skill: ")
  cr.execute(f"delete from skills where name = '{sk}' and user_id = '{choose_user_id}'")

  commit_and_close()
  

def update_skill():

  sk = input("Write Skill Name: ").strip().capitalize()
  prog = input("Write The New Skill Progress: ").strip()
  choose_user_id = input("Please choose which user do you want to update his progress: ")

  cr.execute(f"update skills set progress = '{prog}' where name = '{sk}' and user_id = '{choose_user_id}'")

  commit_and_close()
  

# Check If Command Is Exists
if user_input in commands_list:

  # print(f"Command Found {user_input}")

  if user_input == "s":

    show_skills()
    
  elif user_input == "an":
      
    add_name()
    
  elif user_input == "a":

    add_skill()

  elif user_input == "d":

    delete_skill()
    
  elif user_input == "dn":

    delete_name()

  elif user_input == "u":

    update_skill()
    
  # elif user_input == "ac":
    
  #   add_country()

  else:

    print("App Is Closed.")

else:

  print(f"Sorry This Command \"{user_input}\" Is Not Found")
  
