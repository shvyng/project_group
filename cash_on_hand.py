# code for cash on hand functions

def coh_surplus(csv_data):
    prev_day_coh = float(csv_data[0][1])
    for row in csv_data:
        # if the current day is less than the previous day we know that it is NOT a scenario with a coh surplus
        if float(row[-1]) < prev_day_coh:
            return False
        else:
            
            prev_day_coh = float(row[1])
    #if the return statement was not triggered earlier it means that it is a scenario with a profit surplus
    return True

def calc_coh(csv_data,surpluscheck):
    coh_data = []
    if surpluscheck  == False: 

        # Calculate cash deficit or surplus on each day   
        prev_day_coh = float(csv_data[0][-1])
        day_no = 1
        for row in csv_data:

            # Remove any commas in the COH data
            row[-1] = row[-1].replace(",","")

             # If previous day's COH is higher than current day's COH, append the day number and the difference to coh_data
            if prev_day_coh > float(row[-1]):
                coh_data.append([day_no,(prev_day_coh - float(row[-1]))])
            prev_day_coh = float(row[-1])
            day_no += 1
        return coh_data
    else:

        # Find the day with the highest COH surplus
        highest_surplus = 0
        prev_day_coh = float(csv_data[0][-1])
        highest_day = 0
        day_no = 1
        for row in csv_data:

            # Remove any commas in the COH data
            row[-1] = float(row[-1].replace(",",""))
            current_surplus = row[-1] - prev_day_coh
            if current_surplus > highest_surplus:  # If the current day's COH surplus is higher than the highest surplus found so far, update highest_surplus and highest_day
                highest_surplus = current_surplus
                highest_day = day_no
            day_no += 1
            prev_day_coh = row[-1]
        return([highest_day,highest_surplus])