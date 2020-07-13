#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

r = str(input("Kenestä haetaan tietoa: "))
f = open('data.json', 'r')
data = json.load(f)

print("****\n")
print("Nimi: " + data[r]["Nimi"])
print("Ikä: " + data[r]["Ikä"])
print("Asuinpaikka: " + data[r]["Kaupunki"])
print("Kuvaus: " + data[r]["Kuvaus"])

f.close