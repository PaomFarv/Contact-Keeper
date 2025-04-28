import csv
import os	

class ContactKeeper:
    def __init__(self):
        self.name = []
        self.phone = []
        self.email = []

    def add_contact(self):
        while True:
            name = input("Enter the contact name: ")
            if len(name) < 3:
                print("Name must be at least 3 characters long.")
                continue
            break

        while True:
            phone = input("Enter the contact phone number: ")
            if len(phone) < 10 or not phone.isdigit():
                print("Phone number must be at least 10 digits long and contain only numbers.")
                continue
            break

        while True:
            email = input("Enter the contact email: ")
            if "@" not in email or "." not in email.split("@")[-1]:
                print("Invalid email format.")
                continue
            break

        
        self.name.append(name)
        self.phone.append(phone)
        self.email.append(email)


        with open('contacts.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, phone, email])

        print("Contact added successfully.\n")

    def view_contacts(self):
        file_path = "contacts.csv"
        if not os.path.exists(file_path):
            print("No prior contacts to display.\n")
            return
        
        self.name.clear()
        self.phone.clear()
        self.email.clear()

        with open('contacts.csv', mode='r') as file:
            reader = csv.reader(file)
            print("\n                    << Contacts >>\n")
            print(f"| {'Name':<20} | {'Phone':<25} | {'Email':<30}\n")
            i = 0
            for row in reader:
                name, phone, email = row
                self.name.append(name)
                self.phone.append(phone)
                self.email.append(email)
                
                print(f"{i + 1}. {self.name[i]:<20}{self.phone[i]:<25}{self.email[i]:<30}")
                i += 1
            print("\n")

    def del_contact(self):
        file_path = "contacts.csv"
        if not os.path.exists(file_path):
            print("No prior contacts to display.\n")
            return
        
        self.name.clear()
        self.phone.clear()
        self.email.clear()

        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            print("\n                    << Contacts >>\n")
            print(f"| {'Name':<20} | {'Phone':<25} | {'Email':<30}\n")
            for i, row in enumerate(reader):
                name, phone, email = row
                self.name.append(name)
                self.phone.append(phone)
                self.email.append(email)
                print(f"{i + 1}. {name:<20}{phone:<25}{email:<30}")
            print("\n")

        while True:
            try:
                choice = int(input("Enter the contact number to delete (0 to cancel): "))
                if 1 <= choice <= len(self.name):
                    break
                elif choice == 0:
                    print("Deletion cancelled.")
                    return
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        del self.name[choice - 1]
        del self.phone[choice - 1]
        del self.email[choice - 1]

        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            for i in range(len(self.name)):
                writer.writerow([self.name[i], self.phone[i], self.email[i]]) 
            
        print("Contact deleted successfully.\n")

def main():
    print()
    print("<>"*100)
    print("Welcome to Contact Keeper!")
    print("Choose an option from the following :")
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Delete Contact")
    print("4. Exit")
    print("<>"*100)
    print("\n")

contact_keeper = ContactKeeper() 

while True:
    main()

    user_pick = input("Enter your choice: ")
    
    if user_pick == "1":
        contact_keeper.add_contact()
    elif user_pick == "2":
        contact_keeper.view_contacts()
    elif user_pick == "3":
        contact_keeper.del_contact()
    elif user_pick == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

