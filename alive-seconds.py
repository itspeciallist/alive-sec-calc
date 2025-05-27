from datetime import datetime

def calculate_seconds_alive():
    birth_date_str = input("Enter your birth date (YYYY-MM-DD): ")
    
    try:
        birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")
        now = datetime.now()
        time_alive = now - birth_date
        seconds_alive = int(time_alive.total_seconds())
        print(f"You have been alive for approximately {seconds_alive:,} seconds.")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

calculate_seconds_alive()
