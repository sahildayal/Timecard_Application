# Timecard Tracker

This is a simple Python script to track time cards and save to an Excel file.

## Usage

Run the script and follow the prompts to enter:

- Date (defaults to today)  
- Clock-in time (defaults to now)
- Clock-out time (defaults to now) 
- Task 

The entries will be saved to a Pandas DataFrame and then output to an Excel file called `timecard.xlsx`.

## Requirements

The script requires the following Python packages:

- datetime
- pandas 
- xlsxwriter

Install them via pip:

```
pip install datetime pandas xlsxwriter
```

## Example Output

The Excel file will look something like:

| Date       | Clock In | Clock Out | Task                |  
|------------|----------|-----------|---------------------|
| 2022-10-15 | 09:00    | 17:00     | Grade HW2           |
| 2022-10-16 | 10:00    | 14:00     | Start PSS grading   |
| 2022-10-17 | 08:00    | 12:00     | Mentoring           |

## Improvements to be Made

The script can be customized by:

- Adding validation or constraints on the inputs
- Asking for additional fields like project, category etc
- Changing the DataFrame or Excel formats
- Saving the entries to a database or API instead

## License

This script is released under the MIT License. Feel free to modify and reuse as needed.