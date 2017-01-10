import os
import sys

userlogin = os.getlogin()
oscp = sys.platform
osderect = os.getcwd()
filedirect = os.listdir()

print('имя пользователя:',userlogin)
print('имя операционной системы:',oscp)
print('дериктория в которой лежит программа:',osderect)
print('ближайшие файлы:',filedirect)

close = input('press to enter')




