import os

def main():
    star_eater_1_dict = character()
    star_eater_1 = find_core_type(star_eater_1_dict)

    # print(star_eater_1.print_profile())
    print(star_eater_1.stat_check())

    star_eater_2_dict = character()
    star_eater_2 = find_core_type(star_eater_2_dict)

    # print(star_eater_2.print_profile())
    print(star_eater_2.stat_check())

    if star_eater_1.speed > star_eater_2.speed:
        faster_star_eater = star_eater_1
        slower_star_eater = star_eater_2
    else:
        faster_star_eater = star_eater_2
        slower_star_eater = star_eater_1
    
    print(f"\n{faster_star_eater.name} is faster than {slower_star_eater.name}!\n{faster_star_eater.name} goes first\n")

    while (faster_star_eater.health_check() >= 0) and (slower_star_eater.health_check() >= 0):
        faster_star_eater.fire_laser(slower_star_eater)
        faster_star_eater.special_effects(slower_star_eater)
        if slower_star_eater.health_check() <= 0:
            return 
        slower_star_eater.fire_laser(faster_star_eater)
        slower_star_eater.special_effects(faster_star_eater)

#mother who is proud of her sons
class Star_Eater():
    def __init__(self, name, level, size, special):
        self.name = name
        self.size = size
        self.special = special
        self.__level = int(level)
        self.__health = 30 + self.__level

        self.attack = 9 + self.__level
        self.speed = 9 + self.__level
        self.defense = 9 + self.__level
        self.dodge = 9 + self.__level

    def special_effects(self, target):
        if self.special == "Particles":
            if target.__health <= 0:
                return
            damage = (self.attack // 2) - (target.defense // 2)
            if damage <= 0:
                damage = 1
            print(f"{target.name} has been hit by {self.name}'s particles. they do an aditional {damage} damage!")
            target.take_damage(damage)
        elif self.special == "Binary":
            return self.fire_laser(target)
        else:
            return
        
            
    def stat_check(self):
        return f"Health: {self.__health}\nAttack: {self.attack}\nSpeed: {self.speed}\nDefense: {self.defense}\nDodge: {self.dodge}"
    
    def print_name(self):
        print(f"\nYour selected Star Eater is {self.name}!\n")

    def health_check(self):
        return self.__health
    
    def take_damage(self, damage):
        self.__health -= damage
        if self.__health < 0:
            print(f"{self.name} has lost.")
        else:
            print(f"{self.name} has {self.__health} hit points!")

    def fire_laser(self, target):
        damage = self.attack - (target.defense // 2)
        if damage <= 0:
            damage = 1
        print(f"{self.name} fires a laser at {target.name}. it does {damage} damage!")
        target.take_damage(damage)
            
    
#the sons who are doing their best
class Molten(Star_Eater):
    def __init__(self, name, level, size, special):
        super().__init__(name, level, size, special)
        self.__core_type = "Molten"

        self.attack += 5
        self.speed -= 4
        self.defense -= 4
        self.dodge += 2


    def print_profile(self):
        self.print_name()
        return f"{self.name} is a {self.size}, {self.__core_type} core Star Eater\nThe unique feature they possess is: {self.special}\n"
    
class Common(Star_Eater):
    def __init__(self, name, level, size, special):
        super().__init__(name, level, size, special)
        self.__core_type = "Common"

        #common does not have base stat changes. basic bitch

    def print_profile(self):
        self.print_name()
        return f"{self.name} is a {self.size}, {self.__core_type} core Star Eater\nThe unique feature they possess is: {self.special}\n"
    
class Livable(Star_Eater):
    def __init__(self, name, level, size, special):
        super().__init__(name, level, size, special)
        self.__core_type = "Livable"

        self.attack += 6
        self.speed += 4
        self.defense -= 5
        self.dodge += 2

    def print_profile(self):
        self.print_name()
        print(f"{self.name} is a {self.size}, {self.__core_type} core Star Eater")
        return f"{self.name} is a {self.size}, {self.__core_type} core Star Eater\nThe unique feature they possess is: {self.special}\n"
   
class Void(Star_Eater):
    def __init__(self, name, level, size, special):
        super().__init__(name, level, size, special)
        self.__core_type = "Void"

        self.attack += 10
        self.speed -= 5
        self.defense -= 2
        self.dodge += 3

    def print_profile(self):
        self.print_name()
        print(f"{self.name} is a {self.size}, {self.__core_type} core Star Eater")
        return f"{self.name} is a {self.size}, {self.__core_type} core Star Eater\nThe unique feature they possess is: {self.special}\n"
 
class Synthetic(Star_Eater):
    def __init__(self, name, level, size, special):
        super().__init__(name, level,  size, special)
        self.__core_type = "Synthetic"

        self.attack += 6
        self.speed += 3
        self.defense -= 8
        self.dodge -= 1

    def print_profile(self):
        self.print_name()
        return f"{self.name} is a {self.size}, {self.__core_type} core Star Eater\nThe unique feature they possess is: {self.special}\n"

class Cold(Star_Eater):
    def __init__(self, name, level, size, special):
        super().__init__(name, level,  size, special)
        self.__core_type = "Cold"

        self.attack -= 5
        self.speed += 10
        self.defense += 5
        self.dodge += 3

    def print_profile(self):
        self.print_name()
        return f"{self.name} is a {self.size}, {self.__core_type} core Star Eater\nThe unique feature they possess is: {self.special}\n"
 
#end of classes section
#functions down here just chillin


def select_character_file(): 
    name = input("enter character name: ").lower()
    characterpath = f"stareaters/{name}.txt"
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
    elif star_eater_dict['Core'] == 'Cold':
        core_type = Cold(star_eater_dict['Name'], star_eater_dict['Level'], star_eater_dict['Size'], star_eater_dict['Special'])
        return core_type
    else:
        raise Exception("No valid Core Type was chosen or the Core Type was misspelled. Check character file")
    
main()