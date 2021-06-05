import csv

# This small script modifies our new Dataset and transform it
# so we can reuse code from our exercise and textbook

f = open("modified_data.txt", "w")    # we overwrite existing content
with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            # Replace labels
            # ham = good AND spam = bad
            if (row[1] == 'bad'):
                f.write('spam' + '\t'+ row[0] + '\n')
            else:
                f.write('ham' + '\t'+ row[0] + '\n')
            line_count += 1
    print(f'Processed {line_count} lines.')
f.close()
