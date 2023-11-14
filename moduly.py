# # # #import math
# # # from math import sqrt

# # # print(math.sqrt(10))
# # #==================================
# # import random

# # print(random.randint(1,100))
# # #losowa wartosc z listy
# # fruits = ["apple","banana","orange"]
# # print(random.choice(fruits))

# # #mieszanie listy:
# # numbers=[1,2,3,4,5]
# # random.shuffle(numbers)
# # print(numbers)

# #==============================================================
# #kod ktory wypisze liste wszystkich plikow w biezacym katalogu
# #==============================================================
# import os
# for file in os.listdir():
#     print(file)
# #os.mknod("nowy_plik.txt")
# #==============================================================
# #             Sprawdza czy plik z tą nazwą istnieje
# #==============================================================
# file_path="request.py"
# if os.path.exists(file_path):
#     print('file already exists')

# # print(os.path.isfile(file_path))

# # print(os.listdir('test'))

# # os.rename(file_path, file_path+"nowy_plik.txt")

# # os.mkdir("nowy_katalog")
# # os.mkdir("nowy_katalog")

# # with open("nowy_plik.txt","w") as  f:
# #     f.write("To jest normalny plik.")

# #RegExt 
# #RegExt walidacja e-mail (NA FRONTENDZIE)
# #==============================================================
# #                       daty itp itd
# #==============================================================
# import datetime
# # now = datetime.datetime.now
# # print(now)
# # datetime.datetime.strptime(date,)
# todays_date = datetime.date.today()
# print(todays_date)
#     # %Y - year [0001,...,9999]
#     # %m - month [01,...,12]
#     # %d - day [01,...,31]
#     # %H - hour [00,...,23]

# print(datetime.date.fromtimestamp(10)) #doliczyl 10 sekund
# print(datetime.date.fromtimestamp(10).year)
# a = datetime.time(11, 34, 56)
# print(a.minute)
# print(a.hour)
#################################################################
#               Pobierz aktualną datę i czas
#################################################################
from datetime import datetime, timedelta
now = datetime.now()
print(now)                                  #typ zmiennej - data

print (now.year)
print (now.strftime("%Y"))
#################################################################
#            Wyświetl aktualny miesiąc jako nazwę
#################################################################
now = datetime.now()
print(now.strftime("%B"))
#################################################################
#          konwertuj napis na obiekt daty  2023-11-15
#################################################################
date_object = datetime.strptime("2023-11-15","%Y-%m-%d")
print(date_object)

date_object = datetime.strptime("2023-11-15","%Y-%m-%d")
new_date=date_object + timedelta(days=5)
print(new_date)
#################################################################
#          odejmij dwa tygodnie od aktualnej daty
#################################################################
print(now+timedelta(weeks=-2))            #zmienna z wcześniej
#################################################################
#  Wyświetl różnicę w dniach między 1 stycznia 2023 a dzisiaj
#################################################################
date_first = datetime.strptime("2023-01-01","%Y-%m-%d")
day= now-date_first
print(day.days)

#################################################################
import calendar

#################################################################
#        sprawdź, czy rok 202 jest rokiem przestępnym
#################################################################
new_year= calendar.isleap(2024) #wartosc bool - True/False
print(new_year)
#################################################################
#          Wyświetl numer bieżącego tygodnia roku.
#################################################################
print(now.strftime("%U"))
#################################################################
# Zmień format daty na format RFC 2822
#################################################################
rfc_date=datetime.strptime("2023-11-15 00:00:00", "%Y-%m-%d %H:%M:%S").strftime("%a, %d %b %Y %H:%M:%S +0000")
print(rfc_date)
#################################################################
#       znajdź dzień tygodnia dla 4 lipca bieżącego roku
#################################################################
date2 = datetime(now.year, 7, 4)
print(date2.strftime("%A"))