from os import system
from shutil import move
from glob import glob

files = []
for file in glob("*"):
    files.append(file)

template = input("> ")

for file in files:
        answer = 'n'
        system('clear')
        while answer != 'y':
            print(template)
            season = input("What season?\n")
            episode = input("What episode?\n")
            new_file_name = f"{template} s{season}e{episode}"
            print(new_file_name)
            answer = input("Is this what you want? y/N")

    