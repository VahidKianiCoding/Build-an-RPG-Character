def create_character(name, strength, intelligence, charisma):
    stats = [strength, intelligence, charisma]
    if not isinstance(name, str):
        print("The character name should be a string")
    if name not True:
        print("The character should have a name")
    if len(name) > 10:
        print("The character name is too long")

    if not any(isinstance(s, int) for s in stats):
        print("All stats should be integers")
    if any(for s in stats < 1):
        print("All stats should be no less than 1")
    if any(for s in stats > 4):
        print("All stats should be no more than 4")
    if sum(stats) != 7:
        print("The character should start with 7 points")
