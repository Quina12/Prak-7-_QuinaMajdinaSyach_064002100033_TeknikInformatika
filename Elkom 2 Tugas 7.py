# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 20:35:39 2021

@author: Quina
"""

def jumlah_huruf (kal):
    Jumlah_vokal = 0
    Jumlah_konsonan = 0
    Jumlah_spasi = 0
    for i in range(0, len(string)):
       if string[i] == string[i]=="A" or string[i]=="I" or string[i]=="U" or string[i]=="E" or string[i]=="O" or string[i]=="a" or string[i]=="i" or string[i]=="u" or string[i]=="e" or string[i]=="o":
           Jumlah_vokal += 1
       elif string[i]=="B" or string[i]=="C" or string[i]=="D" or string[i]=="F" or string[i]=="G" or string[i]=="H" or string[i]=="J" or string[i]=="K" or string[i]=="L" or string[i]=="M" or string[i]=="P" or string[i]=="Q" or string[i]=="R" or string[i]=="S" or string[i]=="T" or string[i]=="V" or string[i]=="W" or string[i]=="X" or string[i]=="Y" or string[i]=="Z" or string[i]=="b" or string[i]=="c" or string[i]=="d" or string[i]=="f" or string[i]=="g" or string[i]=="h" or string[i]=="j" or string[i]=="k" or string[i]=="l" or string[i]=="m" or string[i]=="n" or string[i]=="p" or string[i]=="q" or string[i]=="r" or string[i]=="s" or string[i]=="t" or string[i]=="v" or string[i]=="w" or string[i]=="x" or string[i]=="y" or string[i]=="z":
           Jumlah_konsonan += 1
       else :
           Jumlah_spasi += 1
    print("Jumlah banyaknya huruf vokal: ")
    print (Jumlah_vokal)  
    total = Jumlah_konsonan + Jumlah_spasi
    print("Jumlah banyaknya huruf konsonan: ")
    print(total)

print(" @@@    @   @  @@@  @    @      @@")
print("@   @   @   @   @   @@   @     @  @")
print("@ @ @   @   @   @   @ @  @    @@@@@@")
print("@   @   @   @   @   @  @ @   @      @")
print(" @@@ @  @ @ @  @@@  @    @  @        @")

print("\nPROGRAM MENGHITUNG HURUF VOKAL DAN KONSONAN")   
string = list(map(str, input("Masukkan kalimat: ").lower()))
jumlah_huruf(string)  