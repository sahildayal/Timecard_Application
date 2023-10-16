import datetime
import pandas as pd

entries = []

while True:
    date = input("Enter date (YYYY-MM-DD) or press Enter for today's date: ")
    if not date:
        date = datetime.date.today().strftime("%Y-%m-%d")
    
    clock_in = input("Enter clock-in time (HH:MM) or press Enter for now: ") 
    if not clock_in:
        clock_in = datetime.datetime.now().strftime("%H:%M")
    
    clock_out = input("Enter clock-out time (HH:MM) or press Enter for now: ")
    if not clock_out:
        clock_out = datetime.datetime.now().strftime("%H:%M")
        
    task = input("Enter task: ")
    
    entry = {
        'Date': date,
        'Clock In': clock_in,
        'Clock Out': clock_out,
        'Task': task
    }
    
    entries.append(entry)
    
    another = input("Enter another entry? (y/n) ")
    if another.lower() != 'y':
        break
        
df = pd.DataFrame(entries)

writer = pd.ExcelWriter('timecard.xlsx', engine='xlsxwriter') 
df.to_excel(writer, sheet_name='Sheet1', index=False)
writer._save()

print("Timecard saved to timecard.xlsx")