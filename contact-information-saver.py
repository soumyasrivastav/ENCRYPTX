# Contact Management System

def display_menu():
    print("\nContact Management System Menu:")
    print("1. View Contact List")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def view_contacts(contacts):
    if not contacts:
        print("\nNo contacts found.")
    else:
        print("\nContact List:")
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")

def add_contact(contacts):
    name = input("\nEnter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
    print("Contact added.")

def search_contact(contacts):
    search_term = input("\nEnter name or phone number to search: ").lower()
    found_contacts = [contact for contact in contacts if search_term in contact['name'].lower() or search_term in contact['phone']]
    if not found_contacts:
        print("No contacts found.")
    else:
        for contact in found_contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")

def update_contact(contacts):
    search_term = input("\nEnter name or phone number of the contact to update: ").lower()
    for contact in contacts:
        if search_term in contact['name'].lower() or search_term in contact['phone']:
            print(f"Found Contact - Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
            contact['name'] = input("Enter new name: ") or contact['name']
            contact['phone'] = input("Enter new phone number: ") or contact['phone']
            contact['email'] = input("Enter new email: ") or contact['email']
            contact['address'] = input("Enter new address: ") or contact['address']
            print("Contact updated.")
            return
    print("Contact not found.")

def delete_contact(contacts):
    search_term = input("\nEnter name or phone number of the contact to delete: ").lower()
    for contact in contacts:
        if search_term in contact['name'].lower() or search_term in contact['phone']:
            contacts.remove(contact)
            print("Contact deleted.")
            return
    print("Contact not found.")

def main():
    contacts = []
    while True:
        display_menu()
        choice = input("\nChoose an option: ")
        
        if choice == '1':
            view_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
