import json
import os

CONTACTS_FILE = "contacts.json"
contacts = []

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return []

def save_contacts():
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def show_menu():
    print("\n" + "="*40)
    print("      CONTACT MANAGER")
    print("="*40)
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Edit Contact")
    print("5. Delete Contact")
    print("6. Exit")
    print("="*40)

def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    contact = {
        "name": name,
        "phone": phone,
        "email": email if email else "N/A"
    }
    contacts.append(contact)
    save_contacts()
    print(f"{name} added to contacts!")

def view_contacts():
    if not contacts:
        print("\n No contacts found!")
    else:
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. {contact['name']} | {contact['phone']} | {contact['email']}")

def search_contact():
    if not contacts:
        print("\n No contacts to search!")
        return
    
    keyword = input("Enter name or phone to search: ").lower()
    results = []
    
    for contact in contacts:
        if keyword in contact['name'].lower() or keyword in contact['phone']:
            results.append(contact)
    
    if results:
        print(f"\nFound {len(results)} contact(s):")
        for i, contact in enumerate(results, start=1):
            print(f"{i}. {contact['name']} | {contact['phone']} | {contact['email']}")
    else:
        print(" No matching contacts found!")

def edit_contact():
    view_contacts()
    if not contacts:
        return
    
    try:
        num = int(input("\nEnter contact number to edit: "))
        if 1 <= num <= len(contacts):
            contact = contacts[num - 1]
            print(f"Editing: {contact['name']}")
            
            new_name = input(f"New name ({contact['name']}): ").strip()
            new_phone = input(f"New phone ({contact['phone']}): ").strip()
            new_email = input(f"New email ({contact['email']}): ").strip()
            
            if new_name:
                contact['name'] = new_name
            if new_phone:
                contact['phone'] = new_phone
            if new_email:
                contact['email'] = new_email
            
            save_contacts()
            print("Contact updated!")
        else:
            print(" Invalid number!")
    except ValueError:
        print("Please enter a valid number!")

def delete_contact():
    view_contacts()
    if not contacts:
        return
    
    try:
        num = int(input("\nEnter contact number to delete: "))
        if 1 <= num <= len(contacts):
            removed = contacts.pop(num - 1)
            save_contacts()
            print(f"Removed: {removed['name']}")
        else:
            print("Invalid number!")
    except ValueError:
        print("Please enter a valid number!")

contacts = load_contacts()

while True:
    show_menu()
    choice = input("Choose (1-6): ")
    
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        edit_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("\n Goodbye! Contacts saved.")
        break
    else:
        print("Invalid choice! Please enter 1-6.")