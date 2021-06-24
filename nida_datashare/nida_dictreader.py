import glob
import json
import csv
import re
from openpyxl import load_workbook

dict_path = "./inputs/"
data_dictionaries = glob.glob((f"{dict_path}[!~]*.xlsx")) #Ignore temp files
study_metadata = []

# Get study metadata
with open(f"{dict_path}nida_study_metadata.csv") as csvfile:
    reader = csv.reader(csvfile)
    keys = next(reader)
    for row in reader:
        d = {k:v for k,v in zip(keys,row)}
        study_metadata.append(d)

for dictionary in data_dictionaries:
    output_var_list = []
    wb = load_workbook(dictionary)
    print(dictionary)
    study = [d['study_id'] for d in study_metadata if d['data_dictionary_filename'] in dictionary][0]
    for sheet in wb.sheetnames:
        rows = wb[sheet].rows
        # Get keys for each dictionary
        keys = [k.internal_value for k in next(rows)]
        for row in rows:
            # Get values for each dictionary
            values = [k.internal_value for k in row]
            d = {k:v for k,v in zip(keys, values)}
            
            # dataset metadata
            d['dataset'] = sheet
            
            # study ID
            d['study_id'] = study

            # append
            output_var_list.append(d)

    # write variables metadata to JSON
    filename = re.findall(f'[^\{dict_path}].*[^\.xlsx]', dictionary)[0] 
    with open(f"./outputs/{filename}.json", "w") as stream:
        json.dump(output_var_list, stream)

# Write study metadata to JSON
with open(f"./outputs/output_study_list.json", "w") as stream:
    json.dump(study_metadata, stream)
