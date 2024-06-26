import random

# List of syllables to create names
syllables = [
    "bo", "cri", "del", "fa", "ge", "hi", "ja", "ko", "lu", "me", "ni", "po",
    "qua", "re", "su", "ta", "vo", "we", "xi", "yu", "za", "chi", "dro", "fro", "gle"
]

def generate_character_name(used_names):
    
    #Generate a unique character name by combining three random syllables.
    #Ensures that the generated name is not already in the used_names set.

    while True:
        name = random.choice(syllables) + random.choice(syllables) + random.choice(syllables)
        capitalize_name = name.capitalize()
        if capitalize_name not in used_names:
            used_names.add(capitalize_name)
            return capitalize_name

def generate_names(num_names):
    
    #Generate a specified number of unique character names.
    
    used_names = set()
    return [generate_character_name(used_names) for _ in range(num_names)]

def save_names_to_file(names, filename):
    
    #Save the generated names to a file.
    
    try:
        with open(filename, "w") as file:
            for name in names:
                file.write(name + "\n")
        print(f"{len(names)} character names have been generated and saved to '{filename}'.")
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")

def main():
    
    #Main function to generate character names and save them to a file.
    
    try:
        num_names = int(input("Enter the number of character names to generate: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    character_names = generate_names(num_names)
    save_names_to_file(character_names, "character_names.txt")

# Run the main function
if __name__ == "__main__":
    main()
