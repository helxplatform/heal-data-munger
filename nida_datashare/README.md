# NIDA Datashare Parser

This repository contains input files, a python script, and a bash script which, when executed, will convert the contents of the input Excel data dictionary files into a zipped directory of data dictionaries in dbGaP XML format.  The input files were downloaded from the [NIDA Datashare](https://datashare.nida.nih.gov/). Of the 50 files available for download (as of **24 AUG 2021**), 12 were in a sufficiently standardized format as to be read by the script with minor argument changes.  The instructions below detail requirements, installation instructions, and details about the bash script arguments.

## Requirements
It is assumed that those running this script are using Debian-flavored Linux and have bash installed.  Other distros may replace `apt-get`, etc. with the appropriate command.

Enter the following at the command line to install `python3.9` and `python3.9-venv`

```bash
sudo apt-get update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.9
sudo apt-get install python3.9-venv
```

## Clone Repository
Clone repository to your local machine.

## Activating Virtual Environment
After cloning the repository, at the cloned repository root, run the following to set up the virtual environment abd install the appropriate packages:

```bash
python3.9 -m venv venv
source venv/bin/activate
pip install -upgrade pip
pip install -r requirements.txt
```

## Execute the Bash Script
At the repository root, run `bash activate.sh` to run the bash script.

### Bash Script Arguments
The bash script is a wrapper for running the python script (`nida_dictreader.py`) on input data dictionary files with varying arguments.  To understand the arguments that can be specified, run `python3 nida_dictreader.py --help` at the command line.

## Outputs
The outputs are a zipped folder containing all data dictionaries in dbGaP XML format.  The naming convention is `{study_id}.{dataset_id}.xml`.  If the user sets the JSON flag (`-j`) and sets a suitable output path, JSON files containing all datasets within a single study will be output.  The naming convention for JSON files is `{study_id}.json`.
