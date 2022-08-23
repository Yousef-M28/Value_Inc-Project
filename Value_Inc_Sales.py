# Importing libraries
import pandas as pd

# Importing the data file
data = pd.read_csv('transaction.csv', sep=';')

# summary of the data
data.info()

# Cost per transaction
data['CostPricePerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

# Sales per transaction
data['SellingPricePerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

# profit per transaction
data['ProfitPerTransaction'] = data['SellingPricePerTransaction'] - data['CostPricePerTransaction']

# Markup
data['Markup'] = (data['SellingPricePerTransaction'] - data['CostPricePerTransaction']) / data['CostPricePerTransaction']

# Rounding marking
data['Markup'] = round(data['Markup'], 2)

# combining data fields

#checking column data type
print(data['Day'].dtype)

# Change column type
day = data['Day'].astype(str)
year =  data['Year'].astype(str)
print(day.dtype , year.dtype)

date = day +'-' + data['Month'] + '-' + year

data.insert(5, 'Date', date)

# Split the client_keywords field
split_col = data['ClientKeywords'].str.split(',', expand = True)

# Creating new columns for the split column in client keywords
data.insert(13,'ClientAge',split_col[0])
data.insert(14,'ClientType',split_col[1])
data.insert(15,'LengthOfContract',split_col[2])


# Editting the text in columns
data['ClientAge'] = data['ClientAge'].str.replace('[','').str.replace('\'','')
data['ClientType'] = data['ClientType'].str.replace('\'','')
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']','').str.replace('\'','')
data['ItemDescription'] = data['ItemDescription'].str.lower()

# Adding another file
season = pd.read_csv('value_inc_seasons.csv', sep= ';')

# Merging files
data = pd.merge(data, season, on = 'Month')

# Dropping unnecessary columns
data = data.drop(['Day', 'Month', 'Year', 'ClientKeywords'], axis = 1)

# Export into CSV file
data.to_csv('ValueInc_Cleaned.csv', index = False)


