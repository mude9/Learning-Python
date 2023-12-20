# ----------------------------
# -- Loop => While Training --
# ----------------------------
# while condition_is_true
#   Code Will Run Until Condition Become False
# -----------------------

mylist = ["mu", "mi", "ma", "hu", "is", "le"]

# print(len(mylist))  # List Length [5]

a = 0 # a means first index. starts from 0

while a < len(mylist) :
    
    # str to make sure it's string, a+1 means each time add 1 to a, .zfill to add 0 befor the a.
    print(f"#{str(a + 1).zfill(2)} {mylist[a]}") 
    a += 1  # print a + 1 from mylist
    
else:
    print("loop is done")

# print(myF[0])
# print(myF[1])
# print(myF[2])
# print(myF[3])
# print(myF[4])
# print(myF[5])
# print(myF[6])
# print(myF[7])
# print(myF[8])
# print(myF[9])