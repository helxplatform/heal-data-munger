import yaml
import glob
import json
import csv
import re
from openpyxl import load_workbook

'''
colname_transforms - transforms the colnames in the source data dictionaries
to the desired name in the final output.  Assumes homogeneity among all data
dictionaries that are being transformed. It is a dictionary where the key is
current name and value is desired name.

'''
colname_transforms = {
    'FieldName': 'variable_id',
    'Label': 'variable_name',
    'Description': 'variable_description'
}


def nida_raw_to_json(dicts_path, variable_metadata, colname_transforms):
    '''
    Transforms the raw NIDA data and returns single JSON blob of roughly the
    following format:

    [
        {
            "study_id": ,
            "study_name": ,
            "study_description": ,
            ...,
            "datasets": [
                {
                    "dataset_id": ,
                    "dataset_name": ,
                    "dataset_description": ,
                    ...,
                    variables: [
                        {
                            "variable_id": ,
                            "variable_name": ,
                            "variable_description": ,
                            ...
                        },
                        ...,
                    ]
                }
            ]
        }
    ]

    '''
    json_blob = [] # initialize output json blob
   
    for study in study_metadata:
        new_study = study # initialize new study to save back
        dict_filepath = f"{dicts_path}{study['data_dictionary_filename']}"
        new_study.pop('data_dictionary_filename')
        new_study['datasets'] = []
        wb = load_workbook(dict_filepath) 
        for sheet in wb.sheetnames:
            dataset = {} # initialize dataset

            # dataset metadata
            dataset_id = re.sub("[^a-z ]","",sheet.lower()).replace(" ","_")
            dataset['dataset_id'] = dataset_id
            dataset['dataset_name'] = sheet
            dataset['variables'] = []
            
            # variable metadata
            rows = wb[sheet].rows
            
            # filter keys - only keep keys in colname_transforms
            keys = [k.internal_value for k in next(rows)]
            for iteration,row in enumerate(rows):
                print(iteration)
                # Get values for each dictionary
                values = [k.internal_value for k in row]
                variable = {k:v for k,v in zip(keys, values)}
                # variable id
                if not 'variable_id' in variable:
                    print("TODO")
                # Append variable
                dataset['variables'].append(variable)

            # Append dataset
            new_study['datasets'].append(dataset)
        
        json_blob.append(new_study) # add to JSON blob
    
    return(json_blob)

def json_to_dbgap_xml(json_blob):
    '''
    Transforms the JSON blob into a dbGaP XML format, e.g.:

    <data_table id="pht000700.v1" study_id="phs000166.v2" participant_set="1" 
    date_created="Thu Sep  3 15:21:50 2009">

    <variable id="phv00070931.v1">
        <name>SUBJ_ID</name>
        <description>Deidentified Subject ID</description>
        <type>integer</type>
    </variable>
    '''
    return(print("json_to_dbgap_xml"))

dicts_path = "./inputs/"
study_metadata = []

# Import yaml here - transform to appropriate verbiage.

# Get study metadata
with open(f"{dicts_path}nida_study_metadata.csv") as csvfile:
    reader = csv.reader(csvfile)
    keys = next(reader)
    for row in reader:
        d = {k:v for k,v in zip(keys,row)}
        study_metadata.append(d)

# Transform to JSON Blob
json_blob = nida_raw_to_json(dicts_path, study_metadata)

# Debug - write JSON blob
with open(f"./outputs/output_json_blob.json", "w") as stream:
    json.dump(json_blob, stream)