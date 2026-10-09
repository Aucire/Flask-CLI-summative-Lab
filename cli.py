from utills import view_all, view_one, add_item, update_item, delete_item, find_on_api

def main():
    while True:
        print("\n")
        
        print("""
        ===== AN INVENTORY SYSTEM ======
        (Please choose service.)
        1. View all the inventories
        2. View one inventory
        3. Add an inventory
        4. Update price/stock
        5. Delete item
        6. Find item on OpenFoodFacts
        7. Quit
        
    """)
        choice = input("  choice >> ").strip()
        if choice == '7':
            print("Program exited successfully")
            break
        elif choice == '1':
            view_all()
        elif choice == '2':
            view_one()
        elif choice == '3':
            add_item()
        elif choice == '4':
            update_item()
        elif choice == '5':
            delete_item()
        elif choice == '6':
            find_on_api()
        else:
            print(" Invalid choice entered...!")

if __name__ == "__main__":
    main()