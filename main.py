full_dot = "●"
empty_dot = "○"
    

def create_character(name, strength, intelligence, charisma):
    stats={'STR': strength,'INT': intelligence, 'CHA': charisma }
    
    stats_names = []
    stats_values = []
    
    for key, value in stats.items():
        stats_names.append(key)
        stats_values.append(value)
    

    
    if not isinstance(name, str):
        return "The character name should be a string"
    if not name:
        return "The character should have a name"
    if len(name) > 10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"

    
    if not all(isinstance(s, int) for s in stats_values):
        return "All stats should be integers"
    if any(s < 1 for s in stats_values):
        return "All stats should be no less than 1"
    if any(s > 4 for s in stats_values):
        return "All stats should be no more than 4"
    if sum(stats_values) != 7:
        return "The character should start with 7 points"
            
    lines = [name]
    for label, value in zip(stats_names, stats_values):
        lines.append(f"{label} {full_dot * value}{empty_dot * (10 - value)}")
    
    return "\n".join(lines)
    
    

print(create_character('ren', 4, 2, 1))
