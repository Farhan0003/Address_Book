class Contact:
    """Represents a contact in the address book."""

    def __init__(self, first_name, last_name, address, city, state, zip_code, phone_number, email):
        """Initializes the Contact object with personal and contact details."""
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        """Returns a string representation of the contact."""
        return (f"Contact(First Name: {self.first_name}, Last Name: {self.last_name}, Address: {self.address}, "
                f"City: {self.city}, State: {self.state}, Zip: {self.zip_code}, "
                f"Phone: {self.phone_number}, Email: {self.email})")


class AddressBook:
    """Represents an address book that stores multiple contacts."""

    def __init__(self):
        """Initializes the AddressBook with an empty contact list."""
        self.contacts = []

    def add_contact(self, contact):
        """Adds a contact to the address book."""
        try:
            if not isinstance(contact, Contact):
                raise TypeError("Invalid contact. Must be an instance of the Contact class.")
            self.contacts.append(contact)
            print("Contact added successfully!")
        except Exception as e:
            print(f"Error adding contact: {e}")

    def display_contacts(self):
        """Displays all contacts in the address book."""
        try:
            if not self.contacts:
                print("Address Book is empty.")
            else:
                for contact in self.contacts:
                    print(contact)
        except Exception as e:
            print(f"Error displaying contacts: {e}")


def main():
    """Main function to interact with the address book."""
    address_book = AddressBook()
    print("Welcome to the Address Book")

    try:
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        address = input("Enter Address: ")
        city = input("Enter City: ")
        state = input("Enter State: ")
        zip_code = input("Enter Zip: ")
        phone_number = input("Enter Phone Number: ")
        email = input("Enter Email: ")

        if not all([first_name, last_name, address, city, state, zip_code, phone_number, email]):
            raise ValueError("All fields are required.")

        contact = Contact(first_name, last_name, address, city, state, zip_code, phone_number, email)
        address_book.add_contact(contact)
        address_book.display_contacts()

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
