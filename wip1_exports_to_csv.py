import os
import shutil
import csv

from bs4 import BeautifulSoup

INPUT_DIR = 'export/'
OUTPUT_DIR = 'output/exports/'

# clean dir
shutil.rmtree(OUTPUT_DIR, ignore_errors=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

cartels = []
mergers = []
aids = []
aids_ids = set()

files = os.listdir(INPUT_DIR)
for i, filename in enumerate(sorted(files)):
    print(i, filename)
    soup = BeautifulSoup(open(INPUT_DIR + filename).read(), 'html.parser')
    table = soup.find('table')

    headers = [header.text.strip() for header in table.find_all('th')]
    print(len(headers), headers)

    rows = []
    for row in table.find_all('tr'):
        tds = row.find_all('td')
        if len(tds) > 0:
            rows.append([val.text.strip() for val in row.find_all('td')])

    # use .listdir() ordering to detect wich data I'm parsing
    if i == 0:
        mergers = [headers] + rows
    elif i == len(files) - 1:
        cartels = [headers] + rows
    else:
        if len(aids) == 0:
            aids += [headers]
        for row in rows:
            if row[0] not in aids_ids:
                aids_ids.add(row[0])
                aids.append(row)

for filename, data in (('cartels', cartels), ('mergers', mergers), ('aids', aids)):
    with open(OUTPUT_DIR + filename + '.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        for row in data:
            writer.writerow(row)
