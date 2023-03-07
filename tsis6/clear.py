import os

alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
core_path = os.getcwd()
for c in alph:
    file_name = c+".txt"
    path = os.path.join(core_path, file_name)
    os.remove(path)
