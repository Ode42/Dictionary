#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

r = str(input("Kenestä haetaan tietoa: "))
f = open('data.json', 'r')
data = json.load(f)

print("****\n")
print("Name: " + data[r]["Name"])
# print all data you want to print

f.close
