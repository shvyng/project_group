# Contains functions used for calculating profit and loss

def check_net_profit_surplus(csv_data):
    prev_day_profit = float(csv_data.replace(',',''))
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
        prev_day_profit = float(csv_data)
        day_no = 1
        for row in csv_data:
            row [-1] = row[-1].replace (',','')
            if prev_day_profit < float(row[-1]):
