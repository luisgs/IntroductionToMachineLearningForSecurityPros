import csv
from urllib.parse import urlparse

# This small script modifies our new Dataset and transform it
# so we can reuse code from our exercise and textbook

f = open("prevectors.json", "w")    # we overwrite existing content
with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    good = 0
    bad = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            domain = urlparse(row[0]).netloc
            if (row[1] == 'bad'):
                bad+=1
            else:
                good+=1

            url = row[0]
            if not (url.startswith('//') or url.startswith('http://') or url.startswith('https://')):
                url = '//' + url

            f.write('{"code": 200, "content_ssdeep": "12345", "base_url": "' + urlparse(url).netloc + '", "label": "' + row[1] + '", "url": "' + row[0] + '", "offset": "' + row[0].rsplit('/', 1)[-1] + '"}\n')
            line_count += 1
    print(f'Processed {line_count} lines.')
    print(f'Number of GOOD URLs'+str(good))
    print(f'Number of BAD  URLs'+str(bad))
f.close()
