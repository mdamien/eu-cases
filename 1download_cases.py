import os, os.path
from bs4 import BeautifulSoup
import requests
import os
from tqdm import tqdm

os.makedirs('cases', exist_ok=True)

for filename in tqdm(os.listdir('list_pages')):
    soup = BeautifulSoup(open('list_pages/' + filename).read(), 'lxml')
    cases = soup.select('tr .case')
    for case in cases:
        link = case.find('a')
        href = case.find('a').get('href')
        dest_filename = 'cases/%s.html' % href.split('proc_code=')[1]
        if not os.path.exists(dest_filename):
            resp = requests.get('http://ec.europa.eu/competition/elojade/isef/' + href)
            with open(dest_filename, 'w') as f:
                f.write(resp.text)
