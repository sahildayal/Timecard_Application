import datetime
import pandas as pd

def is_within_current_week(date):
    current_date = datetime.date.today()
    current_week_start = current_date - datetime.timedelta(days=current_date.weekday())
    current_week_end = current_week_start + datetime.timedelta(days=6)

    return current_week_start <= date <= current_week_end

date = input("Enter the date (DD/MM/YYYY) or press any key for current date: ")
if not date:
    date = datetime.date.today().strftime("%d/%m/%Y")

clock_in = input("Enter the clock in time (HH:MM AM/PM) or press any key for current time: ")
if not clock_in:
    clock_in = datetime.datetime.now().strftime("%I:%M %p")

clock_out = input("Enter the clock out time (HH:MM AM/PM) or press any key for current time: ")
if not clock_out:
    clock_out = datetime.datetime.now().strftime("%I:%M %p")

clock_out_time = datetime.datetime.strptime(clock_out, "%I:%M %p").time()
if clock_out_time > datetime.time(hour=17):
    print("Warning: Clock out time after 5 PM!")

data = {'Date': [date], 'Clock In': [clock_in], 'Clock Out': [clock_out]}

df = pd.DataFrame(data)

current_week_start = datetime.date.today() - datetime.timedelta(days=datetime.date.today().weekday())
output_file = f'week_{current_week_start.strftime("%Y%m%d")}.xlsx'

try:
    existing_df = pd.read_excel(output_file)
    df = pd.concat([existing_df, df], ignore_index=True)
except FileNotFoundError:
    pass

with pd.ExcelWriter(output_file, mode='a', engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Sheet1', index=False, header=False)

print(f"Clock times saved to {output_file} successfully!")

# output_file = 'clock_times.xlsx'
# df.to_excel(output_file, index=False)
# print(f"Clock times saved to {output_file} successfully!")