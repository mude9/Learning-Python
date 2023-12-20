# ----------------------------------
# -- Practical Membership Control --
# ----------------------------------

# Admin list
Admin = ["Mahmoud", "Mina", "Moaz", "Moutaz"]

# Login
LoginName = input("Plz enter ur name: ").strip().title()

# Conditions
if LoginName in Admin :
    
    print(f"Hi {LoginName}, wlc back")
    Option = input("Wht do u want to do? Update or Delete? ")
    
    #Update Option
    if Option == "Update" or Option == "U" :
      Newname = input("Plz enter new name: ")
      Admin.append(Newname)
      print(f"Mr.{LoginName} Admin list has been Updated")
      print(Admin)
      
    #Update Option
    elif Option == "Delete" or Option == "D" :
        deletedName = input("which user do u want to delete? ")
        Admin.remove(deletedName)
        print(f"Mr.{LoginName} The user name has been deleted and Admin list has been Updated")
        print(Admin)
    
    #Wrong option
    else:
        
        while Option != "Delete" or Option == "D" :
        
        print("sry, wrong option. Plz try again.")

#Not admin        
else :
    Status = input("U r not an Admin. Do u want to add you? \'Yes' or \'No'? ")
    
    #Not admin and want to add
    if Status == "Yes" or Status == "Y" :
        NewAdmin = input(f"MR.{LoginName} plz write new admin name: ")
        Admin.append(NewAdmin)
        print(f"Mr.{LoginName} new admin has been add, here the new Admin list.")
        print(Admin)
    
    #Not admin and want to add    
    elif Status == "No" or Status == "N" :
        print("Thank you for understanding.")
    
    #wrong option    
    else:
        print("Wrong option, plz try again")