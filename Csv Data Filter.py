#Csv Data Filter
# Write a script that reads a CSV file containing employee records
#(Name, Department, Salary), filters
#employees earning above a threshold, and writes them to a new CSV file

import csv

def filter_csv(input_file, output_file, threshold):
    with open(input_file, mode='r', encoding='utf-8') as infile, open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        write.writeheader()
        for row in reader:
            if float(row['Salary']) > threshold:
                writer.writerow(row)
