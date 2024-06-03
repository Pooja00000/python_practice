import csv

# Specify the filename
filename = 'example.csv'

# Open the CSV file
with open(filename, mode='r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Read the header
    header = next(csv_reader)
    print(f'Header: {header}')

    # Read each row
    for row in csv_reader:
        print(row)
