def main():
    character = select_character_file()
    print(open_character_file(character))

def select_character_file(): 
    name = input("enter character name: ") 
    return f"stareaters/SE_{name}.txt"

def open_character_file(character):
    with open(character) as f:
        return f.read()
    
main()