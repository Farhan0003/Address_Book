import logging

logging.basicConfig(filename='Book.log',level=logging.INFO)

address_books = {}
current_address_book = None
class Contact:
    """Class representing a contact in the address book."""

    def __init__(self, first_name, last_name, address, city, state, zip_code, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return (f"Contact(First Name: {self.first_name}, Last Name: {self.last_name}, Address: {self.address}, "
                f"City: {self.city}, State: {self.state}, Zip: {self.zip_code}, "
                f"Phone: {self.phone_number}, Email: {self.email})")


class AddressBook:
    """Class representing the address book which holds multiple contacts."""

    def __init__(self, name):
        self.name = name
        self.contacts = []

    def add_contact(self, contact):
        """Adds a new contact to the address book."""
        try:
            self.contacts.append(contact)
            logging.info(f"Contact added successfully to {self.name}!")
        except Exception as e:
            logging.error(f"Error adding contact: {e}")

    def edit_contact(self, first_name, last_name):
        """Edits an existing contact by first and last name."""
        try:
            for contact in self.contacts:
                if contact.first_name == first_name and contact.last_name == last_name:
                    logging.info(f"Contact found in {self.name}: {contact}")
                    contact.address = input("Enter new Address: ").strip()
                    contact.city = input("Enter new City: ").strip()
                    contact.state = input("Enter new State: ").strip()
                    contact.zip_code = input("Enter new Zip: ").strip()
                    contact.phone_number = input("Enter new Phone Number: ").strip()
                    contact.email = input("Enter new Email: ").strip()
                    logging.info("Contact updated successfully!")
                    return
            logging.warning("Contact not found.")
        except Exception as e:
            logging.error(f"Error editing contact: {e}")

    def delete_contact(self, first_name, last_name):
        """Deletes a contact by first and last name."""
        try:
            for contact in self.contacts:
                if contact.first_name == first_name and contact.last_name == last_name:
                    self.contacts.remove(contact)
                    logging.info("Contact deleted successfully!")
                    return
            logging.warning("Contact not found.")
        except Exception as e:
            logging.error(f"Error deleting contact: {e}")

    def display_contacts(self):
        """Displays all contacts in the address book."""
        try:
            if not self.contacts:
                logging.info(f"Address Book '{self.name}' is empty.")
            else:
                print(f"\nContacts in Address Book: {self.name}")
                for contact in self.contacts:
                    print(contact)
        except Exception as e:
            logging.error(f"Error displaying contacts: {e}")
    @staticmethod
    def search_person(address_books):
        """Search for a person by city or state across multiple address books."""
        if not address_books:
            print("No Address Books available.")
            return

        print("\nSearch Options:")
        print("1. Search by City")
        print("2. Search by State")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            search_term = input("Enter City to search: ").strip()
            search_field = 'city'
        elif choice == '2':
            search_term = input("Enter State to search: ").strip()
            search_field = 'state'
        else:
            print("Invalid choice. Returning to main menu.")
            return

        results_found = False

        for book_name, address_book in address_books.items():
            for contact in address_book.contacts:
                if (search_field == 'city' and contact.city == search_term) or \
                (search_field == 'state' and contact.state == search_term):
                    print(f"\nFound in Address Book: {book_name}")
                    print(contact)
                    results_found = True

        if not results_found:
            print("No contacts found matching the search criteria.")

    @staticmethod
    def count_by_city_or_state(address_books):
        """Count contacts by city or state across multiple address books."""
        if not address_books:
            print("No Address Books available.")
            return

        print("\nCount Options:")
        print("1. Count by City")
        print("2. Count by State")
        choice = input("Enter your choice: ").strip()

        if choice not in ['1', '2']:
            print("Invalid choice. Returning to main menu.")
            return

        count_dict = {}

        for address_book in address_books.values():
            for contact in address_book.contacts:
                key = contact.city if choice == '1' else contact.state
                count_dict[key] = count_dict.get(key, 0) + 1

        print("\nContact Count:")
        for key, count in count_dict.items():
            print(f"{key}: {count} contacts")
    
    def sort_contacts(self, criteria):
        """Sorts contacts in the address book by the given criteria."""
        try:
            if criteria == 'name':
                self.contacts.sort(key=lambda c: c.first_name.lower())
            elif criteria == 'city':
                self.contacts.sort(key=lambda c: c.city.lower())
            logging.info(f"Contacts sorted by {criteria}.")
        except Exception as e:
            logging.error(f"Error sorting contacts: {e}")


def main():
    """Main function to interact with multiple address books."""
    address_books = {}
    current_address_book = None

    print("Welcome to the Address Book System")

    while True:
        print("\n1. Create Address Book\n2. Switch Address Book\n3. Add Contact\n4. Display Contacts\n5. Edit Contact\n6. Delete Contact\n7. Search Person by City or State\n8. Count Contacts by City or State\n9. Sort Contacts Alphabetically\n10. Exit")
        choice = input("Enter your choice: ").strip()

        try:
            if choice == '1':
                book_name = input("Enter new Address Book name: ").strip()
                if book_name in address_books:
                    print("Address Book already exists.")
                else:
                    address_books[book_name] = AddressBook(book_name)
                    current_address_book = address_books[book_name]
                    logging.info(f"Address Book '{book_name}' created and switched to.")
                    print(f"Switched to new Address Book: {book_name}")

            elif choice == '2':
                if not address_books:
                    print("No Address Books available. Create one first.")
                else:
                    print("Available Address Books:", ', '.join(address_books.keys()))
                    book_name = input("Enter Address Book name to switch: ").strip()
                    if book_name in address_books:
                        current_address_book = address_books[book_name]
                        print(f"Switched to Address Book: {book_name}")
                    else:
                        print("Address Book not found.")

            elif choice == '3':
                if current_address_book is None:
                    print("Please create or switch to an Address Book first.")
                else:
                    first_name = input("Enter First Name: ").strip()
                    last_name = input("Enter Last Name: ").strip()
                    address = input("Enter Address: ").strip()
                    city = input("Enter City: ").strip()
                    state = input("Enter State: ").strip()
                    zip_code = int(input("Enter Zip: "))
                    phone_number =int(input("Enter Phone Number: "))
                    email = input("Enter Email: ").strip()

                    contact = Contact(first_name, last_name, address, city, state, zip_code, phone_number, email)
                    current_address_book.add_contact(contact)

            elif choice == '4':
                if current_address_book is None:
                    print("Please create or switch to an Address Book first.")
                else:
                    current_address_book.display_contacts()

            elif choice == '5':
                if current_address_book is None:
                    print("Please create or switch to an Address Book first.")
                else:
                    first_name = input("Enter First Name: ").strip()
                    last_name = input("Enter Last Name: ").strip()
                    current_address_book.edit_contact(first_name, last_name)

            elif choice == '6':
                if current_address_book is None:
                    print("Please create or switch to an Address Book first.")
                else:
                    first_name = input("Enter First Name: ").strip()
                    last_name = input("Enter Last Name: ").strip()
                    current_address_book.delete_contact(first_name, last_name)
            
            elif choice == '7':
                AddressBook.search_person(address_books)

            elif choice == '8':
                AddressBook.count_by_city_or_state(address_books)

            elif choice == '9':
                if current_address_book is None:
                    print("Please create or switch to an Address Book first.")
                else:
                    print("Sort Options:")
                    print("1. Sort by Name")
                    print("2. Sort by City")
                    sort_choice = input("Enter your choice: ").strip()
                    if sort_choice == '1':
                        current_address_book.sort_contacts('name')
                    elif sort_choice == '2':
                        current_address_book.sort_contacts('city')
                    else:
                        print("Invalid choice. Sorting canceled.")
            
            elif choice == '10':
                logging.info("Exiting Address Book System.")
                break

            else:
                print("Invalid choice. Please try again.")

        except Exception as e:
            logging.error(f"Error in main loop: {e}")


if __name__ == "__main__":
    main()
