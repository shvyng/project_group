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