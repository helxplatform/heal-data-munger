#!/bin/bash
set -e

# Specify base directory
FULL_PATH=$(realpath $0)
OUTPUT_BASE=$(dirname $FULL_PATH)
echo $OUTPUT_BASE

# Empty outputs
rm -rf $OUTPUT_BASE/outputs
mkdir $OUTPUT_BASE/outputs

# Files to convert
python3 nida_dictreader.py $OUTPUT_BASE/inputs/CPU0008-Dictionary.xlsx NIDA-CPU-0008 $OUTPUT_BASE/outputs --var-id-column "FieldName" --var-name-column "Label" --var-desc-column "Description"
python3 nida_dictreader.py $OUTPUT_BASE/inputs/CPU0010-Dictionary.xlsx NIDA-CPU-0010 $OUTPUT_BASE/outputs --var-id-column "Field Name" --var-name-column "Field Label" --var-desc-column "Field Description"
python3 nida_dictreader.py $OUTPUT_BASE/inputs/CSP1019_DD.xlsx NIDA-CSP-1019 $OUTPUT_BASE/outputs --var-id-column "Field Name" --var-name-column "Field Label" --var-desc-column "Field Description"
python3 nida_dictreader.py $OUTPUT_BASE/inputs/CSP1020_DD.xlsx NIDA-CSP-1020 $OUTPUT_BASE/outputs --var-id-column "Field Name" --var-name-column "Field Label" --var-desc-column "Field Description"
python3 nida_dictreader.py $OUTPUT_BASE/inputs/CSP1021_DD.xlsx NIDA-CSP-1021 $OUTPUT_BASE/outputs --var-id-column "FIELD NAME" --var-name-column "FIELD LABEL" --var-desc-column "FIELD DESCRIPTION"
python3 nida_dictreader.py $OUTPUT_BASE/inputs/CSP1022_DD.xlsx NIDA-CSP-1022 $OUTPUT_BASE/outputs --var-id-column "FIELD NAME" --var-name-column "FIELD LABEL" --var-desc-column "FIELD DESCRIPTION"
python3 nida_dictreader.py $OUTPUT_BASE/inputs/CTO0007-Dictionary.xlsx NIDA-CTO-0007 $OUTPUT_BASE/outputs --var-id-column "FieldName" --var-name-column "Label" --var-desc-column "Description"
python3 nida_dictreader.py $OUTPUT_BASE/inputs/CTO0008.xlsx NIDA-CTO-0008 $OUTPUT_BASE/outputs --var-id-column "Field Name" --var-name-column "Label"
python3 nida_dictreader.py $OUTPUT_BASE/inputs/CTO0010_DD.xlsx NIDA-CTO-0010 $OUTPUT_BASE/outputs --var-id-column "FieldName" --var-name-column "Label" --var-desc-column "Description"
python3 nida_dictreader.py $OUTPUT_BASE/inputs/CTO0011-DD.xlsx NIDA-CTO-0011 $OUTPUT_BASE/outputs --var-id-column "FieldName" --var-name-column "Label" --var-desc-column "Description"
python3 nida_dictreader.py $OUTPUT_BASE/inputs/MDS0002_DD.xlsx NIDA-MDS-0002 $OUTPUT_BASE/outputs --var-id-column "Field Name" --var-name-column "Field Label" --var-desc-column "Field Description"
python3 nida_dictreader.py $OUTPUT_BASE/inputs/MDS0003-Dictionary.xlsx NIDA-MDS-0003 $OUTPUT_BASE/outputs --var-id-column FieldName --var-id-column "Field Name" --var-name-column "Label"

# Zip up xml files into a tar.gz
tar -czvf $OUTPUT_BASE/outputs/nida_dicts.tar.gz `find $OUTPUT_BASE/outputs | egrep "*.xml"`

# Clean up individual XML files
find $OUTPUT_BASE/outputs/*.xml -exec rm {} +