# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 09:46:48 2021

@author: Quina
"""

print(" @@@    @   @  @@@  @    @      @@")
print("@   @   @   @   @   @@   @     @  @")
print("@ @ @   @   @   @   @ @  @    @@@@@@")
print("@   @   @   @   @   @  @ @   @      @")
print(" @@@ @  @ @ @  @@@  @    @  @        @")   

def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n-1)
        
print("\nPROGRAM MENCARI NILAI FAKTORIAL DARI SEBUAH ANGKA")
n = int(input("Masukan Angka : "))
faktorial(n)
print(f"Nilai faktorialnya adalah {faktorial(n)}")