import os
#--------FIRST--------#
core_path = os.getcwd()
dirlist = os.listdir(core_path)
print(dirlist)
print("Only directories: ", end="")
for dir in dirlist:
    if os.path.isdir(dir):
        print(dir, end=" ")
print("\n")
print("Only files: ", end="")
for file in dirlist:
    if os.path.isfile(file):
        print(file, end=" ")

#--------SECOND--------#
exist_path = os.getcwd()
nonExisting_path = os.path.join(exist_path, "not_here.txt")
nonReadable_path = os.path.join(exist_path, "not_readable.txt")

print('Exist:', os.access(nonReadable_path, os.F_OK))
print('Readable:', os.access(nonReadable_path, os.R_OK))
print('Writable:', os.access(nonReadable_path, os.W_OK))
print('Executable:', os.access(nonReadable_path, os.X_OK))

#--------THIRD--------#
if os.path.exists(core_path):
    print(os.path.split(core_path))

#--------FOURTH--------#
with open("line_num.txt", "r") as f:
    cnt = 0
    for line in f:
        cnt += 1
    print(cnt)

#--------FIFTH--------#
list = ["t1", "t2", "t3"]
with open("fifth.txt", "w") as f:
    for l in list:
        f.write("%s " % l)

#--------SIXTH--------#
alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for c in alph:
    file_name = c+".txt"
    with open(file_name, "w") as f:
        pass

#--------SEVENTH--------#
with open("copy_src.txt", "r") as srcF:
    with open("copy_dest.txt", "w") as destF:
        destF.write(srcF.read())

#--------EIGHTH--------#
path8 = os.path.join(core_path, "must_be_deleted.txt")
access_tuple = (os.access(path8, os.F_OK), os.access(path8, os.R_OK), os.access(path8, os.W_OK), os.access(path8, os.X_OK))
if all(access_tuple):
    os.remove(path8)
else:
    print("access error!")