from bs4 import BeautifulSoup
from slugify import slugify
from pprint import pprint
import os
from tqdm import tqdm
import json

all_cases = []

for filename in tqdm(os.listdir('cases')):
    soup = BeautifulSoup(open('cases/' + filename).read(), 'lxml')
    body = soup.find(id='BodyContent')
    table = body.find('table')

    data = {
        'title': body.find('strong').text.strip(),
        'steps': [],
        # 'html': table.prettify(),
    }

    current_step = None # track if we're parsing a sub-decision

    for row in table.select('tr'):
        tds = row.select('> td')
        if len(tds) == 2:
            label, value = tds
            label = label.text.replace(':','').replace('\t',' ').strip()
            if label:
                date = None
                if ' on ' in label:
                    label, date = label.split(' on ')
                label = slugify(label, separator='_')
                if value.find('table'):
                    value = value.prettify()
                else:
                    value = value.text.replace('\t','').replace('\n\n','').strip()
                
                obj = data
                if current_step != None:
                    obj = current_step
                if date:
                    obj[label] = {
                        'value': value,
                        'date': date,
                    }
                else:
                    obj[label] = value
            else:
                if current_step is not None:
                    data['steps'].append(current_step)
                current_step = {
                    'id': value.text.strip(),
                }
    if current_step is not None:
        data['steps'].append(current_step)

    if len(data['steps']) == 0:
        del data['steps']

    all_cases.append(data)

json.dump(all_cases, open('output/cases.json', 'w'), indent=2, sort_keys=True)