#!/usr/bin/python3


for i in range(0, 400):
    print(f"{i}, {hex(id(i))}")

for j in range(0, 400):
    print(f"{j}, {hex(id(j))}")