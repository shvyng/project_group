#contains overhead functions

def overHead(csv_data):
    highest_expense = 0 # Variable to store the highest expense found so far and initialized to 0
    highest_category = "xx" # Variable to store the category with the highest expense, initialized to "xx"

    # Loop through each row in the CSV data list
    for row in csv_data:
        # Convert the expense value to float and compare it with the current highest_expense
        if float(row[1]) > highest_expense:
            # Convert the expense value to float and compare it with the current highest_expense
            highest_expense = float(row[1])
            # It updates the highest_category to the category name of the current row
            highest_category = row[0]
            
    # Return a list containing the category with the highest expense and its value
    return([highest_category,highest_expense])
    