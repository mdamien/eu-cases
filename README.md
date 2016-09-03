# EU Competition cases

Extract all the cases from http://ec.europa.eu/competition/elojade/isef/index.cfm

To use, first install the dependencies: `pip3 install -r req.txt`

Then, there are two dataset you can get, `cases.json` with detailed infos or the CSVs with not many infos (but easier to process):

### `cases.json`
What it does: going though all the results pages to get all the cases links and download those cases and then parse them

 - that's the `0get_list.py`, `1download_cases.py`, `2parse_cases.py` scripts
 - you get `output/cases.json` at the end

### the CSVs 

What it does: do an export of each case category:

 - that's `wip0_get_exports.py` and `wip1_exports_to_csv.py`
 - you get `mergers.csv`, `aids.csv` and `cartels.csv` at the end in `output/export/`

Example of exploitation of the CSVs: https://fusiontables.google.com/data?docid=1KGQ-EQUqhnQv05s-DgKWS1JU2LAG_fW-i1rFGM4Y#rows:id=1 

## TODO

 - [ ] manage to download the cases based on the export list
 - [ ] automate and make the data and stats available online

