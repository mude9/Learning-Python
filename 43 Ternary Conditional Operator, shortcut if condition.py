# ----------------------------------
# -- Ternary Conditional Operator --
# ----------------------------------

country = "A"

if country == "Egypt" : print(f"The Weather in {country} Is 15")
elif country == "KSA" : print(f"The Weather in {country} Is 30")
else : print("Country is Not in The List")

# Short If

movieRate = 18
age = int(input("age: "))

if age < movieRate :

  print("Movie S Not Good 4U") # Condition If True

else :

  print("Movie S Good 4U And Happy Watching") # Condition If False

print("Movie S Not Good 4U" if age < movieRate else "Movie S Good 4U And Happy Watching")

# Condition If True | If Condition | Else | Condition If False