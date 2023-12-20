# -------------------------------------
# -- File Handling => Important Info --
# -------------------------------------

import os

myFile = open("D:\Python\Files\osama.txt", "a")
myFile.truncate(5)  # اقتطاع عدد معين من الجملة اللي مكتوبة في الفايل

myFile = open("D:\Python\Files\osama.txt", "a")
print(myFile.tell()) # قولي الماوس موحود فين بالظبط

myFile = open("D:\Python\Files\osama.txt", "r")
myFile.seek(11) # حرك مكان الماوس لمكان معين
print(myFile.read())

import os

os.remove("D:\Python\Files\osama.txt")