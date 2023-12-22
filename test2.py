import csv
def modify_values(value):
    if value in ['Neu', 'SPos', 'SNeg', 'Neg']:
        return 'NoPos'
    return value

# Read data.csv and create modified_data.csv
with open('anno_study.csv', mode='r') as file:
    with open('pos_study.csv', mode='w', newline='') as modified_file:
        reader = csv.reader(file)
        writer = csv.writer(modified_file)


        # Modify values and write to the new file
        for row in reader:
            modified_row = [modify_values(value) for value in row]
            writer.writerow(modified_row)

print("Modified CSV file 'neu_study.csv' has been created.")