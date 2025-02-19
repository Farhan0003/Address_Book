import logging

logging.basicConfig(filename='Book.log',level=logging.INFO)

class Contact:
    """Represents a contact with personal details."""

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
    """Manages a collection of contacts."""

    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        try:
            if not isinstance(contact, Contact):
                raise TypeError("Expected a Contact instance.")
            self.contacts.append(contact)
            logging.info("Contact added successfully!")
        except Exception as e:
            logging.error(f"Error adding contact: {e}")

    def display_contacts(self):
        try:
            if not self.contacts:
                logging.info("Address Book is empty.")
            for contact in self.contacts:
                print(contact)
        except Exception as e:
            logging.error(f"Error displaying contacts: {e}")


def main():
    """Runs the Address Book application."""

    address_book = AddressBook()

    logging.info("Welcome to the Address Book")

    while True:
        print("\n1. Add Contact\n2. Display Contacts\n3. Exit")
        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                first_name = input("Enter First Name: ")
                last_name = input("Enter Last Name: ")
                address = input("Enter Address: ")
                city = input("Enter City: ")
                state = input("Enter State: ")
                zip_code = input("Enter Zip: ")
                phone_number = input("Enter Phone Number: ")
                email = input("Enter Email: ")

                contact = Contact(first_name, last_name, address, city, state, zip_code, phone_number, email)
                address_book.add_contact(contact)

            elif choice == '2':
                address_book.display_contacts()

            elif choice == '3':
                logging.info("Exiting Address Book.")
                break

            else:
                logging.warning("Invalid choice. Please try again.")
        except Exception as e:
            logging.error(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
