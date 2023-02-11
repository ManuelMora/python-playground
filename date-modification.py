from datetime import datetime

today = datetime.today()
today = today.replace(hour=1, minute=0, second=0, microsecond=0)
print(f"Toda's date: {today}")
