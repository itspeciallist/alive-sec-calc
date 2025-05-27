from datetime import datetime

def calculate_seconds_alive():
    birth_date_str = input("Sheikvanet dab tarighi (YYYY-MM-DD): ")
    
    try:
        birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")
        now = datetime.now()
        time_alive = now - birth_date
        seconds_alive = int(time_alive.total_seconds())
        print(f"tqven khart {seconds_alive:,} tsamis")
    except ValueError:
        print("arastsori formati. gtkhovt gamoikenot YYYY-MM-DD.")

calculate_seconds_alive()
