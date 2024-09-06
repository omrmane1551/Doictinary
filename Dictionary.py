# Define a dictionary to store words and their definitions
dictionary = {
    "python": "A high-level programming language known for its readability and simplicity.",
    "data": "Information that is collected and analyzed to draw conclusions.",
    "algorithm": "A step-by-step procedure for solving a problem or performing a task."
}

def display_menu():
    print("\nInteractive Dictionary")
    print("1. Look up a word")
    print("2. Add a new word")
    print("3. Update an existing word")
    print("4. Delete a word")
    print("5. Exit")

def lookup_word():
    word = input("Enter the word to look up: ").lower()
    definition = dictionary.get(word)
    if definition:
        print(f"{word.capitalize()}: {definition}")
    else:
        print(f"'{word}' not found in the dictionary.")

def add_word():
    word = input("Enter the new word: ").lower()
    if word in dictionary:
        print(f"'{word}' already exists in the dictionary.")
    else:
        definition = input(f"Enter the definition for '{word}': ")
        dictionary[word] = definition
        print(f"'{word}' has been added to the dictionary.")

def update_word():
    word = input("Enter the word to update: ").lower()
    if word in dictionary:
        definition = input(f"Enter the new definition for '{word}': ")
        dictionary[word] = definition
        print(f"'{word}' has been updated.")
    else:
        print(f"'{word}' not found in the dictionary.")

def delete_word():
    word = input("Enter the word to delete: ").lower()
    if word in dictionary:
        del dictionary[word]
        print(f"'{word}' has been deleted.")
    else:
        print(f"'{word}' not found in the dictionary.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            lookup_word()
        elif choice == '2':
            add_word()
        elif choice == '3':
            update_word()
        elif choice == '4':
            delete_word()
        elif choice == '5':
            print("Exiting the dictionary. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()
