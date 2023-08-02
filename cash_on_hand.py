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