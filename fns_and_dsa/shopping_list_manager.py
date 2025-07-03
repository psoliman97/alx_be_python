def display_menu():
    print("Shopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

def main():
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            item = input("Enter the item to add: ").strip()
            shopping_list.append(item)
        elif choice == '2':
            item = input("Enter item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                print(f"Item '{item}' not found in the list.")
        elif choice == '3':
            print("Shopping List:")
            for item in shopping_list:
                print(item)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()