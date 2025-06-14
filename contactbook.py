contact = {}

def display_contacts():
    print("\nName\t\tContact Number")
    print("-" * 30)
    for name, number in contact.items():
        print(f"{name}\t\t{number}")
    print()

while True:
    print("\n==== Contact Book Menu ====")
    print("1. Add New Contact")
    print("2. Search Contact")
    print("3. Display All Contacts")
    print("4. Edit Contact")
    print("5. Delete Contact")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice (1-6): "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        name = input("Enter contact name: ").strip()
        phone = input("Enter mobile number: ").strip()
        if name in contact:
            print("Contact already exists. Use Edit option to update.")
        else:
            contact[name] = phone
            print("Contact added successfully!")

    elif choice == 2:
        search_name = input("Enter contact name to search: ").strip()
        if search_name in contact:
            print(f"{search_name}'s number is {contact[search_name]}")
        else:
            print("Contact not found.")

    elif choice == 3:
        if not contact:
            print("Contact book is empty.")
        else:
            display_contacts()

    elif choice == 4:
        edit_name = input("Enter contact name to edit: ").strip()
        if edit_name in contact:
            new_number = input("Enter new number: ").strip()
            contact[edit_name] = new_number
            print("Contact updated successfully!")
        else:
            print("Contact not found.")

    elif choice == 5:
        del_name = input("Enter contact name to delete: ").strip()
        if del_name in contact:
            confirm = input(f"Are you sure you want to delete '{del_name}'? (y/n): ").lower()
            if confirm == 'y':
                del contact[del_name]
                print("Contact deleted successfully!")
            else:
                print("Deletion cancelled.")
        else:
            print("Contact not found.")

    elif choice == 6:
        print("Exiting Contact Book. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
