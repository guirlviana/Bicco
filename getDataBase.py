import os

def get_data_base():
    for file in os.listdir():
        name, ext = os.path.splitext(file)
        if ext == '.db':
            pathdb = os.path.join(os.getcwd(), name + ext)
            break
    return pathdb


