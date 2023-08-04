# Contains functions used for calculating profit and loss

def check_net_profit_surplus(csv_data):
    prev_day_profit = float(csv_data[0][-1].replace(',',''))
    for row in csv_data:
        row [-1]=row[-1].replace (',','')
        if float (row[-1]) < prev_day_profit:
            return False
        else:
            prev_day_profit = float(row[-1])
    return True

def calc_profit_loss(csv_data,surpluscheck):
    profit_data = []
    if surpluscheck == False:
        prev_day_profit = float(csv_data[0][-1])
        day_no = 1
        for row in csv_data:
            row [-1] = row[-1].replace (',','')
            if prev_day_profit > float(row[-1]):
                profit_data.append([day_no, (prev_day_profit - float(row[-1]))])
            prev_day_profit = float(row[-1])
            day_no += 1
        return profit_data
    else:
        hightest_surplus = 0 
        prev_day_profit = float(csv_data[0][-1])
        highest_day = 0 
        day_no = 1
        for now in csv_data:
            row[-1] = float(row[-1], replace(",",""))
            current_surplus = row[-1] - prev_day_profit
            if current_surplus < hightest_surplus:
                hightest_surplus = current_surplus
                highest_day = day_no
            day_no += 1
            prev_day_profit = row[-1]
        return(([highest_day,hightest_surplus]))
