import sys
from access_logs import view_access_logs
from vehicle_management import add_staff_vehicle, add_visitor_vehicle

def main_menu():
    while True:
        print("\n=== Vehicle Authentication System ===")
        print("1. Add Staff Vehicle")
        print("2. Add Visitor Vehicle")
        print("3. View Access Logs")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == "1":
            staff_name = input("Enter staff name: ")
            plate_number = input("Enter plate number: ")
            add_staff_vehicle(staff_name, plate_number)
            
        elif choice == "2":
            visitor_name = input("Enter visitor name: ")
            plate_number = input("Enter plate number: ")
            add_visitor_vehicle(visitor_name, plate_number)
            
        elif choice == "3":
            view_access_logs()
            
        elif choice == "4":
            print("Thank you for using the system!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    print("Connecting to Vehicle Auth System API...")
    # We could add a health check here if we wanted, but for now let's just run the menu
    main_menu()