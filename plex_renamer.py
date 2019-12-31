from os import system
from shutil import move
from glob import glob

files = []
for file in glob("*"):
    files.append(file)

for file in files:
    print(file)
template = input("What's the name of the show?\n")

for file in files:
        answer = 'n'
        system('clear')
        while answer != 'y':
            print(file)
            season = input("What season?\n")
            episode = input("What episode?\n")
            file_type = input("Wait, whats the file extension?\n")
            new_file_name = f"{template} s{season}e{episode}.{file_type}"
            print(new_file_name)
            answer = input("Is this what you want? y/N\n")
        move(file, new_file_name)

    