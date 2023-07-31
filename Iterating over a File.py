with open("Myfile.txt","r") as f:
    for line in iter(f.readline,""):
        print(line)

with open("Myfile.txt","r") as f:
    for line in iter(f.readlines()):
        print(line)


with open("Myfile.txt", "r") as f:
    for line in iter(f.readline()):
        print(line)