import pandas as pd

# Load the dataset from the specified file path
file_path = r'C:\Users\Me\Downloads\Customer_Call_List.xlsx'
df = pd.read_excel(file_path)

# Print the original DataFrame
print("Original DataFrame:")
print(df)

# Handle missing values
df.fillna('', inplace=True)

# Standardize phone numbers by removing non-numeric characters
df['Phone_Number'] = df['Phone_Number'].str.replace(r'[^0-9]', '', regex=True)

# Handle empty phone numbers
df['Phone_Number'] = df['Phone_Number'].replace('', 'Unknown')

# Normalize boolean columns
df['Paying Customer'] = df['Paying Customer'].replace({'Yes': True, 'Y': True, 'No': False, 'N': False, 'TRUE': True, 'FALSE': False})
df['Do_Not_Contact'] = df['Do_Not_Contact'].replace({'Yes': True, 'Y': True, 'No': False, 'N': False, 'TRUE': True, 'FALSE': False})

# Ensure all boolean columns are filled and converted to boolean type
df['Paying Customer'] = df['Paying Customer'].astype(bool)
df['Do_Not_Contact'] = df['Do_Not_Contact'].astype(bool)

# Remove unnecessary columns
df.drop(columns=['Not_Useful_Column'], inplace=True)

# Clean 'First_Name' and 'Last_Name' columns
df['First_Name'] = df['First_Name'].str.strip().str.title()
df['Last_Name'] = df['Last_Name'].str.strip().str.title()

# Clean 'Address' column
df['Address'] = df['Address'].str.strip()

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Print the cleaned DataFrame
print("\nCleaned DataFrame:")
print(df)



