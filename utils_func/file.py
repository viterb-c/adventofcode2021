import os

def get_lines(file_path):
    if os.path.exists(file_path):
        file = open(file_path, 'r')
        lines = file.readlines()
        return lines
    return []