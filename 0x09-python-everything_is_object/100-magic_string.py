#!/usr/bin/python3
def magic_string(iteration=[0]):
    iteration[0] += 1
    return str("BestSchool, " * (iteration[0] - 1)) + "BestSchool"
