import requests
from datetime import datetime

API_URL = "http://localhost:5000/api"

def add_staff_vehicle(staff_name, plate_number):
    try:
        response = requests.post(f"{API_URL}/staff", json={
            "name": staff_name,
            "plate_number": plate_number
        })
        
        if response.status_code == 201:
            print(f"\nStaff vehicle added successfully! (ID: {response.json().get('id')})")
        else:
            print(f"\nError adding staff vehicle: {response.json().get('error', 'Unknown error')}")
            
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to server: {e}")

def add_visitor_vehicle(visitor_name, plate_number):
    valid_until = input("Enter validity date (YYYY-MM-DD): ")
    # Append time to make it ISO format compatible with backend expectation if needed, 
    # but backend expects ISO. Let's try to send as is or format it.
    # Backend: datetime.fromisoformat(expiry.replace('Z', '+00:00'))
    # So we should send ISO string.
    
    try:
        # Basic validation/formatting
        expiry_dt = datetime.strptime(valid_until, "%Y-%m-%d")
        expiry_iso = expiry_dt.isoformat()
        
        response = requests.post(f"{API_URL}/visitors", json={
            "name": visitor_name,
            "plate_number": plate_number,
            "expiry": expiry_iso
        })
        
        if response.status_code == 201:
            print(f"\nVisitor vehicle added successfully! (ID: {response.json().get('id')})")
        else:
            print(f"\nError adding visitor vehicle: {response.json().get('error', 'Unknown error')}")
            
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to server: {e}")

# Deprecated/Unused functions in new API-driven model, but kept for compatibility if imported elsewhere
def log_access(identifier, plate_number, action, details):
    print("Logging is now handled by the server.")

def is_staff_vehicle(plate_number):
    print("Check is now handled by the server.")
    return False

def get_staff_name(plate_number):
    return None

def check_vehicle_access(plate_number):
    # We can use the process-vehicle endpoint here
    try:
        response = requests.post(f"{API_URL}/process-vehicle", json={
            "plate_number": plate_number,
            "direction": "IN" # Defaulting to IN for check
        })
        data = response.json()
        print(f"Access Status: {data.get('status')} - {data.get('message')}")
    except requests.exceptions.RequestException as e:
        print(f"Error checking access: {e}")