import os

def main():
    character = select_character_file()
    print(open_character_file(character))

def select_character_file(): 
    name = input("enter character name: ").lower()
    characterpath = f"stareaters/SE_{name}.txt"
    if os.path.isfile(characterpath):
        return characterpath
    else:
        raise Exception("Character does not Exist")

def open_character_file(character):
    with open(character) as f:
        return f.read()
    
main()