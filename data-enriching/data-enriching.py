#Importing Pandas
import pandas as pd 

#Importing CSV Files
Neighborhood_Atlas = pd.read_csv(r'C:/Users/emman/Documents/GitHub/data-enrichment/Neighborhood Atlas/Neighborhood_Atlas.csv')
SPARCS = pd.read_csv(r'C:/Users/emman/Documents/GitHub/data-enrichment/SPARCS/SPARCS.csv')

# Changin all data types to string 
Neighborhood_Atlas= Neighborhood_Atlas.astype(str)
SPARCS = SPARCS.astype(str)

#Deleting Duplicates and Empty Rows
Neighborhood_Atlas = Neighborhood_Atlas.drop_duplicates(keep='first')
Neighborhood_Atlas = Neighborhood_Atlas.dropna()
SPARCS = SPARCS.drop_duplicates(keep='first')
SPARCS = SPARCS.dropna()

#Formatting Neighborhood_Atlas['ZIPID'] to 3 Digit Code in order to align with  SPARCS['ZIPID': 'Zip Code - 3 digits']
Neighborhood_Atlas['ZIPID'] = Neighborhood_Atlas['ZIPID'].str.slice(1, 4)
#Deleting First 2 Columns of Neighborhood_Atlas
Neighborhood_Atlas = Neighborhood_Atlas.drop(Neighborhood_Atlas.columns[[0, 1, ]], axis=1)  
#Changing 'ZIPID' column titled to 'Zip Code - 3 digits' in order to allow for merging by column
Neighborhood_Atlas = Neighborhood_Atlas.rename(columns={'ZIPID': 'Zip Code - 3 digits'})

# Showing Proof of Workability, by deleting alot of  rows, if not then it would give error saying not emough disk space
N = 1000000
SPARCS.drop(index=SPARCS.index[:N], axis=0, inplace=True)
Neighborhood_Atlas = Neighborhood_Atlas.head(3000)
SPARCS= SPARCS.head(3000)

#Merging both DataFrames by Matching 3 Digit Zip Code
Enriched_SPARCS = Neighborhood_Atlas.merge(SPARCS, how = 'inner', on = ['Zip Code - 3 digits'])

#Exporting to CSV
Enriched_SPARCS.to_csv("C:/Users/emman/Documents/GitHub/data-enrichment/Enriched_SPARCS/Enriched_SPARCS.csv")
print(Enriched_SPARCS)
