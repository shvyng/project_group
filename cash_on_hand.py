def coh_surplus(csv_data):
    try: #Double check required if the code could be used
        prev_day_coh = float(csv_data[0][-1])
        for row in csv_data[1:]:
            if float(row[-1]) < prev_day_coh:
                return False
            else:
                prev_day_coh = float(row[-1])
        return True
    except (ValueError, IndexError):#Double check required if the code could be used
        return False#Double check required if the code could be used
    
def process_coh_data(data):
    coh_data = []  # List to store day number and COH difference pairs
    prev_day_coh = None  # Variable to store previous day's COH
    day_no = 1  # Day number starts from 1
    
    for row in data:
        if prev_day_coh is not None and prev_day_coh > float(row[-1]):#Double check required if the code could be used
            coh_difference = prev_day_coh - float(row[-1])#Double check required if the code could be used
        prev_day_coh = float(row[-1])
        day_no += 1
    return coh_data

highest_surplus = 0
prev_day_coh = float(csv_data[0][-1])
highest_day = 0
for day_no, row in enumerate(csv_data, start=1):#Double check required if the code could be used
# The variable `day_no` can now be used outside the loop if needed.