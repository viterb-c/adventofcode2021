import os

def get_lines(file_path):
    if os.path.exists(file_path):
        file = open(file_path, 'r')
        lines = file.read().splitlines()
        return lines
    return []