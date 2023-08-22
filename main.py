import datetime
import pandas as pd

date = input("Enter the date (DD/MM/YYYY) or press any key for current date: ")
if not date:
    date = datetime.date.today().strftime("%d/%m/%Y")

clock_in = input("Enter the clock in time (HH:MM AM/PM) or press any key for current time: ")
if not clock_in:
    clock_in = datetime.datetime.now().strftime("%I:%M %p")

clock_out = input("Enter the clock out time (HH:MM AM/PM) or press any key for current time: ")
if not clock_out:
    clock_out = datetime.datetime.now().strftime("%I:%M %p")

data = {'Date': [date], 'Clock In': [clock_in], 'Clock Out': [clock_out]}

df = pd.DataFrame(data)

output_file = 'clock_times.xlsx'
df.to_excel(output_file, index=False)
print(f"Clock times saved to {output_file} successfully!")