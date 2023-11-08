import os

def main():
    star_eater_1_dict = character()
    core_type_1 = find_core_type(star_eater_1_dict)
    
    star_eater_1 = core_type_1
    print(core_type_1.print_profile())

class Star_Eater():
    def __init__(self, name, level):
        self.name = name
        self.__level = level

    def print_name(self):
        print(f"\nYour selected Star Eater is {self.name}!\n")
    
class Molten(Star_Eater):
    def __init__(self, name, level, size, special):
        super().__init__(name, level)
        self.size = size
        self.special = special
        self.__core_type = "Molten"

    def print_profile(self):
        self.print_name()
        return f"{self.name} is a {self.size}, {self.__core_type} core Star Eater\nThe unique feature they possess is: {self.special}\n"

class Common(Star_Eater):
    def __init__(self, name, level, size, special):
        super().__init__(name, level)
        self.size = size
        self.special = special
        self.__core_type = "Common"

    def print_profile(self):
        self.print_name()
        return f"{self.name} is a {self.size}, {self.__core_type} core Star Eater\nThe unique feature they possess is: {self.special}\n"
        
class Livable(Star_Eater):
    def __init__(self, name, level, size, special):
        super().__init__(name, level)
        self.size = size
        self.special = special
        self.__core_type = "Livable"

    def print_profile(self):
        self.print_name()
        print(f"{self.name} is a {self.size}, {self.__core_type} core Star Eater")
        return f"{self.name} is a {self.size}, {self.__core_type} core Star Eater\nThe unique feature they possess is: {self.special}\n"

class Void(Star_Eater):
    def __init__(self, name, level, size, special):
        super().__init__(name, level)
        self.size = size
        self.special = special
        self.__core_type = "Void"

    def print_profile(self):
        self.print_name()
        print(f"{self.name} is a {self.size}, {self.__core_type} core Star Eater")
        return f"{self.name} is a {self.size}, {self.__core_type} core Star Eater\nThe unique feature they possess is: {self.special}\n"

class Synthetic(Star_Eater):
    def __init__(self, name, level, size, special):
        super().__init__(name, level)
        self.size = size
        self.special = special
        self.__core_type = "Synthetic"

    def print_profile(self):
        self.print_name()
        return f"{self.name} is a {self.size}, {self.__core_type} core Star Eater\nThe unique feature they possess is: {self.special}\n"

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

def character():
    star_eater = select_character_file()
    star_eater_file = open_character_file(star_eater)
    star_eater_information = get_character_information(star_eater_file)
    return star_eater_information

def find_core_type(star_eater_dict):
    if star_eater_dict['Core'] == 'Molten':
        core_type = Molten(star_eater_dict['Name'], star_eater_dict['Level'], star_eater_dict['Size'], star_eater_dict['Special'])
        return core_type
    elif star_eater_dict['Core'] == 'Common':
        core_type = Common(star_eater_dict['Name'], star_eater_dict['Level'], star_eater_dict['Size'], star_eater_dict['Special'])
        return core_type
    elif star_eater_dict['Core'] == 'Livable':
        core_type = Livable(star_eater_dict['Name'], star_eater_dict['Level'], star_eater_dict['Size'], star_eater_dict['Special'])
        return core_type
    elif star_eater_dict['Core'] == 'Void':
        core_type = Void(star_eater_dict['Name'], star_eater_dict['Level'], star_eater_dict['Size'], star_eater_dict['Special'])
        return core_type
    elif star_eater_dict['Core'] == 'Synthetic':
        core_type = Synthetic(star_eater_dict['Name'], star_eater_dict['Level'], star_eater_dict['Size'], star_eater_dict['Special'])
        return core_type
    else:
        raise Exception("No valid Core Type was chosen or the Core Type was misspelled. Check character file")
    
main()