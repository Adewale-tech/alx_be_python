def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"'{item}' has been added to your shopping list.\n")

        elif choice == 2:
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from your shopping list.\n")
            else:
                print(f"'{item}' not found in your shopping list.\n")

        elif choice == 3:
            print("\nYour Shopping List:")
            if not shopping_list:
                print("The shopping list is currently empty.")
            else:
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            print()

        elif choice == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
