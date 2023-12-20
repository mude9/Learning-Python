# --------------------------
# -- Membership Operators --
# --------------------------
# in
# not in
# --------------------------

# String

name = "Osama"
print("s" in name)
print("a" in name)
print("A" in name)

print("#" * 50)

# List

friends = ["Ahmed", "Sayed", "Mahmoud"]
print("Osama" in friends)
print("Sayed" in friends)
print("Mahmoud" not in friends)

print("#" * 50)

# Using In and Not In With Condition

name = str(input("What is you name? ")).strip().title()
countrylistone = ["Egypt", "Qater", "china", "KSA", "Palastin"]
countrylistonedis = 90

countrylisttwo = ["USA", "Italy", "UK"]
countrylisttwodis = 20

courseprice = 120


country = str(input("please enter your country: "))

if country in countrylistone :
    print(f"Hi {name} cuz u r from {country}, u have {countrylistonedis}% discount, so course price is {courseprice - countrylistonedis}")
    
elif country in countrylisttwo :
    print(f"Hi {name} cuz u r from {country}, u have {countrylisttwodis}% discount, so course price is {courseprice - countrylisttwodis}")

else:
    print("SRY u have no discount")