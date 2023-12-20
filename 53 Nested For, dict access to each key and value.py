# -----------------
# -- Loop => For --
# -- Nested Loop --
# -----------------

peoples = ["Osama", "Ahmed", "Sayed", "Ali"]

skills = ['Html', 'Css', 'Js']

for name in peoples:  # Outer Loop

  print(f"{name} Skills Is: ")

  for skill in skills:  # Inner Loop

    print(f"- {skill}")

# Dictionary

peoples = {
  "Osama": {
    "Html": "70%",
    "Css": "80%",
    "Js": "70%"
  },
  "Ahmed": {
    "Html": "90%",
    "Css": "80%",
    "Js": "90%"
  },
  "Sayed": {
    "Html": "70%",
    "Css": "60%",
    "Js": "90%"
  }
}
# name => keys
for name in peoples:
        # name => keys: osama, ahmed, sayed
  print(f"Skills and Progress For {name} Is: ")
  
        # skills => the second keys: html, css, Js
  for skill in peoples[name]:
      
        # print each key "name" with each skill "html, css, Js" for each name
    print(f"{skill.upper()} => {peoples[name][skill]}")