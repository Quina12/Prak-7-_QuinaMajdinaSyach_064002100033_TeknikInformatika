# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 23:16:28 2021

@author: Quina
"""

print(" @@@    @   @  @@@  @    @      @@")
print("@   @   @   @   @   @@   @     @  @")
print("@ @ @   @   @   @   @ @  @    @@@@@@")
print("@   @   @   @   @   @  @ @   @      @")
print(" @@@ @  @ @ @  @@@  @    @  @        @")

def power(num):
    power = num ** 3
    return power

def check(num):
    if num%3==0:
        return power(num)
    else:
        return False
        
while True:
    print("\nPROGRAM PENGECEKAN BILANGAN")
    num = int(input("Masukan bilangan : "))
    print(f"Hasil: {check(num)}")