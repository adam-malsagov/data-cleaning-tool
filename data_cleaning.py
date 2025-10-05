import pandas as pd
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

# Load dataset into a pandas DataFrame
file_path = input("Enter the dataset CSV file path: ")
df = pd.read_csv(file_path)
print(Fore.YELLOW + "Current columns:", list(df.columns))

# Remove missing values
df.isnull()
new_df = df.dropna(axis=0).dropna(axis=1)

# Rename columns and standardize text formatting
rename_cols = input("Enter columns to rename (e.g. First Name:first_name) separated by commas (or press Enter to skip): ")
if rename_cols.strip():
    new_names = dict(pair.split(":") for pair in rename_cols.split(","))
    new_df.rename(columns=new_names, inplace=True)

    cols_format = list(new_names.values())
    for col in cols_format:
        if col in new_df.columns:
            new_df[col] = new_df[col].str.lower().str.strip().str.replace(r"[^a-z\s]", "", regex=True)

# Summary report
original_rows, original_cols = df.shape
final_rows, final_cols = new_df.shape
rows_removed = original_rows - final_rows
cols_removed = original_cols - final_cols
print(Fore.BLACK + Back.WHITE + "<===== SUMMARY =====>")
print(f"Rows removed: {rows_removed}")
print(f"Columns removed: {cols_removed}")

if rename_cols.strip():
    print(f"Renamed columns: {new_names}")
    print(f"Standardized columns: {cols_format}")

# Save data to new CSV file
print(Fore.BLACK + Back.WHITE + "<===== SAVED DATA =====>")
print(Fore.GREEN + "Cleaned data is saved to cleaned_data.csv")
new_df.to_csv("cleaned_data.csv", index=False)