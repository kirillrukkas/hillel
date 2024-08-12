import csv

RANDOM_MICHAELS = r"work_with_csv\random-michaels.csv"
RMC_CSV = r"work_with_csv\rmc.csv"



def main():
    all_data = []
    for  file_name in [RMC_CSV, RANDOM_MICHAELS]:
        all_data += get_cvs_data(file_name)
    
    data_without_duplicates = []    
    for row in all_data:
        if row in data_without_duplicates:
            print(f"String {row} is duplicate")
            continue
        else:
            data_without_duplicates.append(row)
    
    print(f"There are {len(all_data) - len(data_without_duplicates)} duplicates")
   
    
    with open('output.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data_without_duplicates)
    

def get_cvs_data(file_name):
    rows = []
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            rows.append(row)
    return rows


if __name__ == '__main__':
    main()
    print ("All done")



