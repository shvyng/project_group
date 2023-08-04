# contains overhead functions

def overHead(csv_data):
    # Variable to store the category with the highest expense, initialized to 0
    highest_expenses = 0
    #  Variable to store the category with the highest, expense, intialized to "xx"
    highest_category

    # Loop through each row in the CSV data list
    for row in csv_data:
        # Convert the expense value to float and compare it with the current highest_expense
        highest_expense = float(row[1])
        # It updates the highest_category to the categiry name of the current row
        highest_category = row[0]

    # Return a list cotaining the category with the highest expense and its value
    return([highest_category, highest_expense])