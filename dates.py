import re

# Define the regular expression pattern
date_pattern = re.compile(r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/([12][0-9]{3})$')

# Test strings
test_dates = [
    '31/02/2020', # Non-existent date
    '31/04/2021', # Non-existent date
    '29/02/2020', # Leap year
    '29/02/2021', # Non-leap year
    '30/04/2021', # Valid date
    '01/12/2022', # Valid date
    '12/31/2022', # Invalid format
]

# Iterate through each test date
for date_string in test_dates:
    # Match the date pattern
    match = date_pattern.match(date_string)
    
    if match:
        # Extract day, month, and year from the matched string
        day, month, year = match.groups()
        
        # Convert day, month, and year strings to integers
        day = int(day)
        month = int(month)
        year = int(year)
        
        # Check if the date is valid
        valid_date = True
        if month in [4, 6, 9, 11] and day > 30:
            valid_date = False
        elif month == 2:
            if day > 29:
                valid_date = False
            elif day == 29 and not (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
                valid_date = False
        elif day > 31:
            valid_date = False
        
        # Output the result
        if valid_date:
            print(f"{date_string} is a valid date.")
        else:
            print(f"{date_string} is not a valid date.")
    else:
        print(f"{date_string} is not in the correct format.")
