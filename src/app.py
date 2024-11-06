import pandas as pd

# Load each CSV file
file_1 = pd.read_csv('C:/Users/rushi/OneDrive/Desktop/Projects/3. Forage_Quantium_SDE Certification/quantium-starter-repo/data/daily_sales_data_0.csv')
file_2 = pd.read_csv('C:/Users/rushi/OneDrive/Desktop/Projects/3. Forage_Quantium_SDE Certification/quantium-starter-repo/data/daily_sales_data_1.csv')
file_3 = pd.read_csv('C:/Users/rushi/OneDrive/Desktop/Projects/3. Forage_Quantium_SDE Certification/quantium-starter-repo/data/daily_sales_data_2.csv')

# Display the first few rows of each file to inspect the structure
print(file_1.head())
print(file_2.head())
print(file_3.head())

# Normalize the 'product' column by converting it to lowercase and removing spaces
file_1['product'] = file_1['product'].str.lower().str.strip()
file_2['product'] = file_2['product'].str.lower().str.strip()
file_3['product'] = file_3['product'].str.lower().str.strip()

# Filter the data to keep only 'pink morsel' (case-insensitive)
file_1 = file_1[file_1['product'] == 'pink morsel']
file_2 = file_2[file_2['product'] == 'pink morsel']
file_3 = file_3[file_3['product'] == 'pink morsel']

# Calculate sales as quantity * price
# Remove '$' from price and convert it to a numeric value for calculation
file_1['price'] = file_1['price'].replace({'\$': ''}, regex=True).astype(float)
file_2['price'] = file_2['price'].replace({'\$': ''}, regex=True).astype(float)
file_3['price'] = file_3['price'].replace({'\$': ''}, regex=True).astype(float)

# Calculate sales
file_1['sales'] = file_1['quantity'] * file_1['price']
file_2['sales'] = file_2['quantity'] * file_2['price']
file_3['sales'] = file_3['quantity'] * file_3['price']

# Select the relevant columns: sales, date, region
file_1 = file_1[['sales', 'date', 'region']]
file_2 = file_2[['sales', 'date', 'region']]
file_3 = file_3[['sales', 'date', 'region']]

# Combine all three files into one DataFrame
combined_data = pd.concat([file_1, file_2, file_3], ignore_index=True)

# Save the combined data to a new CSV file
combined_data.to_csv('formatted_sales_data.csv', index=False)

# Optional: Check the output
print("Formatted Data:")
print(combined_data.head())
