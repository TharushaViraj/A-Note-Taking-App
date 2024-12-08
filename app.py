# Author : Tharusha Viraj
import os

# File to store notes
NOTES_FILE = "notes.txt"

def display_menu():
    """Display the menu options to the user."""
    print("\n--- Note-Taking Application ---")
    print("1. View Notes")
    print("2. Add Note")
    print("3. Delete Notes")
    print("4. Exit")

def view_notes():
    """Display the saved notes."""
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as file:
            notes = file.readlines()
            if notes:
                print("\nYour Notes:")
                for i, note in enumerate(notes, 1):
                    print(f"{i}. {note.strip()}")
            else:
                print("\nNo notes found.")
    else:
        print("\nNo notes found.")

def add_note():
    """Add a new note."""
    note = input("\nEnter your note: ")
    with open(NOTES_FILE, "a") as file:
        file.write(note + "\n")
    print("Note added successfully!")

def delete_notes():
    """Delete all saved notes."""
    if os.path.exists(NOTES_FILE):
        os.remove(NOTES_FILE)
        print("\nAll notes deleted successfully!")
    else:
        print("\nNo notes to delete.")

def main():
    """Main function to run the app."""
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")
        if choice == "1":
            view_notes()
        elif choice == "2":
            add_note()
        elif choice == "3":
            delete_notes()
        elif choice == "4":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid option. Please try again.")

# Main function
if __name__ == "__main__":
    main()
