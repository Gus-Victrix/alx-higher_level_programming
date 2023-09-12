#!/usr/bin/python3

"""
Add a new line in file after a line that contain a key word
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Add a new line in file after a line that contain a key word
    Args:
        filename (file): Name of a file
        search_string (str): The string to search
        new_string (str): The string to fill
    Returns: Anything
    """
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
        line_list = []
        for line in lines:
            line_list.append(line)
            if search_string in line:
                line_list.append(new_string)
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(line_list)
