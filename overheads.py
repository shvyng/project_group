#contains overhead functions

def overHead(csv_data): # Variable to store the category with the highest expense, initialized to 0
    highest_expense = 0  # Variable to store the category with the highest, expense, intialized to "xx"
    highest_category = "xx"

      # Loop through each row in the CSV data list
    for row in csv_data:
        if float(row[1]) > highest_expense: # Convert the expense value to float and compare it with the current highest_expense
            highest_expense = float(row[1])
            highest_category = row[0] # It updates the highest_category to the categiry name of the current row
    
    return([highest_category,highest_expense])   # Return a list cotaining the category with the highest expense and its value
    