from pathlib import Path
import csv
import profit_loss
import overheads
import cash_on_hand

# Main folder of project 

##---------------------------------FUNCTION TO EXTRACT AND READ CSV FILE ---------------------------------------------

def read_csv(file_name):
     #create file reader
    fp=Path.cwd()/f"csv_reports/{file_name}"
    
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header

 # create an empty lists to store time sheet and sales record
        csvData=[] 

 # append time sheet and sales record into the salesRecords list
        for row in reader:
            temp = []
         # GET ROW DATA AND APPEND IT INTO csvData variable
            for i in range(len(row)):
                temp.append(row[i])
            csvData.append(temp)
    return csvData;

def main():
# CALL READ CSV FUNCTION TO READ CSV FILES
    
    overHeads_csv = read_csv("overheads.csv")
    cashOnHand_csv = read_csv("Cash On Hand.csv")
    profitAndLoss_csv = read_csv("Profit_and_Loss.csv")

 # Calculate the highest overhead from the overheads data
    highest_overhead = overheads.overHead(overHeads_csv)
    
 # Check if the net profit is a surplus or deficit
    check_profit_surplus = profit_loss.check_net_profit_surplus(profitAndLoss_csv)
 # Calculate the profit or loss for each day from the profit and loss data
    profit_loss_data = profit_loss.calc_profit_loss(profitAndLoss_csv,check_profit_surplus)
    
 # Check if the cash on hand is a surplus or deficit and then it calculates the cash on hand csv data
    check_coh_surplus = cash_on_hand.coh_surplus(cashOnHand_csv)
    coh_data = cash_on_hand.calc_coh(cashOnHand_csv,check_coh_surplus)
    
    
# Create a summary report file named "summary_report.txt"
    write_path = Path.cwd()/"summary_report.txt"

# Write the summary report to the file
    with write_path.open(mode="w", encoding="UTF-8", newline="") as file:
        file.write("[HIGHEST OVERHEAD] {overHead_category}: {overHead_expense}%\n".format(overHead_category = highest_overhead[0],overHead_expense = highest_overhead[1]))
        if check_coh_surplus == True:
            file.write("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")
            file.write("[HIGHEST CASH SURPLUS] DAY: {dayNum}, AMOUNT: USD{surplusAmount}\n".format(dayNum=coh_data[0], surplusAmount=int(coh_data[1])))
        else:
            for row in coh_data:
                file.write("[CASH DEFICIT] DAY: {dayNum}, AMOUNT: USD{surplusAmount}\n".format(dayNum=row[0], surplusAmount=int(row[1])))

        if check_profit_surplus == True:
            file.write("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")
            file.write("[HIGHEST NET PROFIT SURPLUS] DAY: {dayNum}, AMOUNT: USD{surplusAmount}\n".format(dayNum=profit_loss_data[0], surplusAmount=int(profit_loss_data[1])))
        else:
            for row in profit_loss_data:
                file.write("[PROFIT DEFICIT] DAY: {dayNum}, AMOUNT: USD{surplusAmount}\n".format(dayNum=row[0], surplusAmount=int(row[1])))

        file.close()

main()