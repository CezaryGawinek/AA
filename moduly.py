# # #import math
# # from math import sqrt

# # print(math.sqrt(10))
# #==================================
# import random

# print(random.randint(1,100))
# #losowa wartosc z listy
# fruits = ["apple","banana","orange"]
# print(random.choice(fruits))

# #mieszanie listy:
# numbers=[1,2,3,4,5]
# random.shuffle(numbers)
# print(numbers)

#==============================================================
#kod ktory wypisze liste wszystkich plikow w biezacym katalogu
#==============================================================
import os
for file in os.listdir():
    print(file)
#os.mknod("nowy_plik.txt")
#==============================================================
#             Sprawdza czy plik z tą nazwą istnieje
#==============================================================
file_path="request.py"
if os.path.exists(file_path):
    print('file already exists')

# print(os.path.isfile(file_path))

# print(os.listdir('test'))

# os.rename(file_path, file_path+"nowy_plik.txt")

# os.mkdir("nowy_katalog")
# os.mkdir("nowy_katalog")

# with open("nowy_plik.txt","w") as  f:
#     f.write("To jest normalny plik.")

#RegExt 
#RegExt walidacja e-mail (NA FRONTENDZIE)
#==============================================================
#                       daty itp itd
#==============================================================
import datetime
# now = datetime.datetime.now
# print(now)
# datetime.datetime.strptime(date,)
todays_date = datetime.date.today()
print(todays_date)
    # %Y - year [0001,...,9999]
    # %m - month [01,...,12]
    # %d - day [01,...,31]
    # %H - hour [00,...,23]

print(datetime.date.fromtimestamp(10)) #doliczyl 10 sekund
print(datetime.date.fromtimestamp(10).year)
a = datetime.time(11, 34, 56)
print(a.minute)
print(a.hour)