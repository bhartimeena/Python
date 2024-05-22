import sys
from recycling_system import RecyclingSystem

def main():
    system = RecyclingSystem()
    
    while True:
        print("\nRecycling Reward System")
        print("1. Add Item")
        print("2. View Total Reward")
        print("3. Reset System")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            item_type = input("Enter item type (A, B, or C): ").strip().upper()
            system.add_item(item_type)
        elif choice == '2':
            print(f"Total Reward: INR{system.get_total_reward():.2f}")
        elif choice == '3':
            system.reset()
            print("System reset successful.")
        elif choice == '4':
            print("Exiting system.")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
