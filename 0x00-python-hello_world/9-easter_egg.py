#!/usr/bin/python3
file_path = "The_Zen_of_Python.txt"
with open(file_path, "r") as file:
    content = file.read()
    print(content)
