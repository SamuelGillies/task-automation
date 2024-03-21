import os
import csv

csv_file = './data/data.csv'
source_directory = './source'
input_suffix = '.JPG'
destination_directory = './output'


def main():
    # Read CSV file
    with open(csv_file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        
        # Skip header if present
        next(csvreader, None)
        
        # Iterate through CSV rows
        for row in csvreader:
            old_filename = os.path.join(source_directory, row[0])
            new_filename_single = os.path.join(destination_directory, row[1] + ', ' + row[2] + ' - ' + row[3] + input_suffix)
            new_filename_multi = os.path.join(destination_directory, row[1] + ', ' + row[2] + ' - ' + row[3] + ', ' + row[4] + input_suffix)

            # Check if the file exists before renaming
            if os.path.exists(old_filename):
                if row[4].strip(): 
                    os.rename(old_filename,  new_filename_multi)
                    print(f'Renamed {row[0]} to {row[1] + ", " + row[2] + " - " + row[3] + ", " + row[4] + input_suffix}')
                else: 
                    os.rename(old_filename,  new_filename_single)
                    print(f'Renamed {row[0]} to {row[1] + ", " + row[2] + " - " + row[3] + input_suffix}')
            else:
                print(f'File not found: {row[0]}')

    print('File conversion complete')

if __name__ == '__main__':
    main()