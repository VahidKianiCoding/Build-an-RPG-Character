def create_character(name, strength, intelligence, charisma):
    stats = [strength, intelligence, charisma]
    if not isinstance(name, str):
        print("The character name should be a string")
    if name not True:
        print("The character should have a name")
    if len(name) > 10:
        print("The character name is too long")
