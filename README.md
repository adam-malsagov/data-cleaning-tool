# Data Cleaning Tool 

## Overview
This script:
1. Loads a CSV dataset into a Pandas DataFrame.
2. Removes rows or columns containing missing values.
3. Allows the user to rename selected columns.
4. Standardizes text formatting **only in renamed columns**:
   - Converts to lowercase  
   - Trims whitespace  
   - Removes special characters
5. Generates a summary report of changes.
6. Saves the cleaned dataset to `cleaned_data.csv`.

## Usage
1. Install dependencies:
```bash
pip install -r requirements.txt
```
2. Run the script:
```bash
python data_cleaning.py
```
3. Provide:
   - Path to the CSV file (e.g., `sample_data.csv`)
   - Rename mapping in the format `OldName:NewName`, separated by commas.

## Example
Input CSV:
```
Name,Age,Occupation
 Alice ,25,Engineer
Bob!,,Designer
,30,Artist
Carol ,29,Writer
```

Run:
```
Enter the dataset CSV file path: sample_data.csv
Enter columns to rename as old:new: Name:Full Name,Occupation:Job
```

Result (`cleaned_data.csv`):
```
full name,age,job
alice,25,engineer
carol,29,writer
```