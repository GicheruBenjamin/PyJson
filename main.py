

''' Enrty point for the program '''
''' Takes input from the user as per the questions and 
then does the action based on the option choosen by the user '''

from Services import Create, Read, Update, Delete

def main():
    while True:
        print("\nWelcome to the PyJson CLI App")
        print("Choose an option:")
        print("1. Create a user")
        print("2. Read a user")
        print("3. Update a user")
        print("4. Delete a user")
        print("5. List all users")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            name = input("Enter name: ")
            age = input("Enter age: ")
            location = input("Enter location: ")
            user_id = Create.create_user(name, age, location)
            print(f"User created with id: {user_id}")
        
        elif choice == '2':
            user_id = input("Enter user id to read: ")
            user = Read.read_user(user_id)
            if user:
                print(f"\nUser ID: {user_id}")
                print(f"Name: {user['name']}")
                print(f"Age: {user['age']}")
                print(f"Location: {user['location']}")
            else:
                print("User not found.")
        
        elif choice == '3':
            user_id = input("Enter user id to update: ")
            print("Leave field blank if no change is needed.")
            name = input("Enter new name: ").strip() or None
            age = input("Enter new age: ").strip() or None
            location = input("Enter new location: ").strip() or None
            if Update.update_user(user_id, name, age, location):
                print("User updated successfully.")
            else:
                print("User not found.")
        
        elif choice == '4':
            user_id = input("Enter user id to delete: ")
            if Delete.delete_user(user_id):
                print("User deleted successfully.")
            else:
                print("User not found.")
        
        elif choice == '5':
            all_users = Read.read_all()
            if all_users:
                print("\nCurrent users:")
                for uid, details in all_users.items():
                    print(f"ID: {uid} -> {details}")
            else:
                print("No users found.")
        
        elif choice == '6':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
