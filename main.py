import os

def main():
    character = select_character_file()
    character_file = open_character_file(character)
    Character_information = get_character_information(character_file)

    print(f"\nYour selected Star Eater is {Character_information['Name']}!\n")
    print(f"{Character_information['Name']} is a {Character_information['Size']}, {Character_information['Core']} core Star Eater")
    print(f"The unique feature they possess is: {Character_information['Special']}")

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
    
def get_character_information(character):
    character_info_list = character.splitlines()
    character_dict = {}
    for i in character_info_list:
        character_dict[i.split('-')[0]] = i.split('-')[1]
    return character_dict
    
main()