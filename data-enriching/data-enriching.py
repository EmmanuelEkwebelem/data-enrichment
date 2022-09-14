
import pandas as pd 

Neighborhood_Atlas = pd.read_csv(r'C:/Users/emman/Desktop/data-enrichment/Neighborhood Atlas/US_2019_ADI_Census Block Group_v3.1.csv')
SPARCS = pd.read_csv(r'C:/Users/emman/Desktop/data-enrichment/SPARCS/Hospital_Inpatient_Discharges__SPARCS_De-Identified___2015.csv')

Neighborhood_Atlas = Neighborhood_Atlas.drop_duplicates(keep='first')
Neighborhood_Atlas = Neighborhood_Atlas.dropna()

SPARCS = SPARCS.drop_duplicates(keep='first')
SPARCS = SPARCS.dropna()

Neighborhood_Atlas= Neighborhood_Atlas.astype(str)
SPARCS = SPARCS.astype(str)

for (columnName, columnData) in Neighborhood_Atlas.iteritems():
    Neighborhood_Atlas.replace('[^A-Za-z0-9]+', ' ', regex=True)
    Neighborhood_Atlas.replace(' ', '')

for (columnName, columnData) in SPARCS.iteritems():
    SPARCS.replace('[^A-Za-z0-9]+', ' ', regex=True)
    SPARCS.replace(' ', '')



