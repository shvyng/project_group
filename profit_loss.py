# Contains functions used for calculating profit and loss

def check_net_profit_surplus(csv_data):
    # Replace commas in CSV so that we can convert to a float type
    prev_day_profit = float(csv_data[0][-1].replace(",",""))
    for row in csv_data:
        row[-1] = row[-1].replace(",","")
        # If the current day is less than the previous day we know that it is NOT a scenario with a profit surplus
        if float(row[-1]) < prev_day_profit:
            return False
        else:
            prev_day_profit = float(row[-1])
    #If the return statement was not triggered earlier it means that it is a scenario with a profit surplus
    return True



def calc_profit_loss(csv_data,surpluscheck):
    profit_data = []
    if surpluscheck  == False:    
        # Calculate daily profit or loss
        prev_day_profit = float(csv_data[0][-1])
        day_no = 1
        for row in csv_data:
            # Remove any commas in the profit/loss data
            row[-1] = row[-1].replace(",","") 
            if prev_day_profit > float(row[-1]):
                # If previous day's profit is higher than current day's profit, append the day number and the difference to profit_data
                profit_data.append([day_no,(prev_day_profit - float(row[-1]))])
            prev_day_profit = float(row[-1])
            day_no += 1
        return profit_data
    else:
        # Find the day with the highest surplus
        highest_surplus = 0
        prev_day_profit = float(csv_data[0][-1])
        highest_day = 0
        day_no = 1
        for row in csv_data:
            # Remove any commas in the profit/loss data
            row[-1] = float(row[-1].replace(",",""))
            current_surplus = row[-1] - prev_day_profit
            if current_surplus > highest_surplus:
                # If the current day's surplus is higher than the highest surplus found so far, update highest_surplus and highest_day
                highest_surplus = current_surplus
                highest_day = day_no
            day_no += 1
            prev_day_profit = row[-1]
        return([highest_day,highest_surplus])


