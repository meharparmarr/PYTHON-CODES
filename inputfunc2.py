def calculate_character_count(name):
    return len(name)

def main():
    name = input("Enter a name: ")
    character_count = calculate_character_count(name)
    print(f"The number of characters in the name '{name}' is: {character_count}")

if __name__ == "__main__":
    main()
