import requests
from datetime import datetime

API_URL = "http://localhost:5000/api"

def view_access_logs():
    try:
        response = requests.get(f"{API_URL}/access-logs")
        
        if response.status_code == 200:
            logs = response.json()
            
            print("\nAccess Logs")
            print("-" * 80)
            
            for log in logs:
                name = log.get('name') or "Unknown"
                plate = log.get('plate')
                status = log.get('status')
                message = log.get('reason')
                # Timestamp from API is ISO format
                try:
                    dt = datetime.fromisoformat(log.get('timestamp'))
                    time_str = dt.strftime('%Y-%m-%d %I:%M:%S %p')
                except:
                    time_str = log.get('timestamp')
                
                # Color coding for status
                status_color = "\033[92m" if "GRANTED" in str(status) else "\033[91m"
                reset_color = "\033[0m"
                
                print(f"{name} ({plate})".ljust(40) + f"{time_str}".rjust(40))
                print(f"Status: {status_color}{status}{reset_color} - {message}\n")
        else:
            print(f"Error retrieving logs: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to server: {e}")

def log_access(name, plate_number, status, message):
    # This is now handled by the server automatically
    pass

def initialize_access_logs_table():
    # Handled by server migration
    pass