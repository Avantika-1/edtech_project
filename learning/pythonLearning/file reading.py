import csv

# Specify the path to your CSV file
filename = 'C:\Admin\Downloads\Jira Export Excel CSV (my defaults) 20250115110120'

# Open the CSV file and read its contents
with open(filename, mode='r') as file:
    csv_reader = csv.reader(file)

    # Skip the header if there's one
    next(csv_reader)  # Use only if there's a header

    # Loop through each row in the CSV file
    for row in csv_reader:
        print(row)
