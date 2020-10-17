############################################ Imports #############################################

import Acquire

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

######################################## Prep Zillow Data ########################################

def prepare_zillow():
    '''
    Acquire and prepare the zillow data obtained from the SQL database.
    Nulls are removed/replaced, outliers are removed, new features are created,
    and columns are renamed/rearranged. Returns the prepped df.
    '''
    # acquire the data from module
    df = acquire.get_home_data()
    
    # Removing Nulls from Columns
    # sets thresh hold to 75 percent nulls, if more than %25 nulls it will be removed
    threshold = df.shape[0] * .75

    # remove columns with specified threshold
    df = df.dropna(axis=1, thresh=threshold)
    
    # Removing Nulls from Rows
    # sets thresh hold to 75 percent nulls, if more than %25 nulls it will be removed
    thresh_hold = df.shape[1] * .75

    # remove rows with specified threshold
    df = df.dropna(axis=0,thresh=thresh_hold)
    
    # Removing Columns with Repeated Data/Unecessary Data
    # don't need additional sqft, county id/city, assessment year, and census columns
    df = df.drop(columns=['finishedsquarefeet12', 'regionidcounty', 'rawcensustractandblock',
                          'regionidcity','assessmentyear'], axis=1)
    
    # Removing Outliers from Continuous Variables
    # assigning columns to remove outliers
    columns = ['calculatedfinishedsquarefeet','lotsizesquarefeet','structuretaxvaluedollarcnt',
           'landtaxvaluedollarcnt','taxamount']
    
    # looping through continuous variables to remove outliers
    for x in columns:
    
        # calculate IQR
        Q1 = df[x].quantile(0.25)
        Q3 = df[x].quantile(0.75)
        IQR = (Q3 - Q1) * 1.5
        
        # calculate upper and lower bounds, outlier if above or below these
        upper = Q3 + (1.5 * IQR)
        lower = Q1 - (1.5 * IQR)
    
        # creates df of values that are within the outlier bounds
        df = df[(df[x] > (lower)) | (df[x] < (upper))]
        
    # Filling Leftover Nulls by Columns
    # Full Bathroom Count Nulls
    # mode of bathroomcnt
    fullbath_mode = df.fullbathcnt.mode()[0]
    # filling nulls with the mode
    df['fullbathcnt'] = df.fullbathcnt.fillna(fullbath_mode)
    
    # Region Zip Code Nulls
    # filling with 90000 to represent no known zipcode (0 would skew the data)
    df['regionidzip'] = df.regionidzip.fillna(90_000)
    
    # Year Built Nulls
    # average of property year built
    year_avg = round(df.yearbuilt.mean())
    # filling nulls with average year built
    df['yearbuilt'] = df.yearbuilt.fillna(year_avg)
    
    # Census Tract and Block Nulls
    # mode of census tract and block
    census_mode = df.censustractandblock.mode()[0]
    # filling nulls with mode
    df['censustractandblock'] = df.censustractandblock.fillna(mode)
    
    # Feature Engineering - creating columns
    # calculating bed+bath from 0 null columns of bedroom/bathroom count
    df['bed_plus_bath'] = df.bathroomcnt + df.bedroomcnt
    # droping original calculated field that had nulls
    df = df.drop('calculatedbathnbr',axis=1)
    
    # Property Age
    # current year minus year built
    df['age'] = 2020 - df.yearbuilt
    
    # Transaction Month
    # converting date to string to use split method
    df['transactiondate'] = df.transactiondate.astype('str')
    # creating new feature as the second index (month) of the transaction date split
    df['transaction_month'] = df.transactiondate.str.split('-',expand=True)[1]
    
    # Renaming Columns
    df.columns = ['index_id', 'parcel_id', 'bathrooms', 'bedrooms', 'property_sqft', 'county_id', 'full_bathrooms',
                  'latitude', 'longitude', 'lot_sqft', 'land_use_code', 'land_use_type', 'zip_code', 'room_count',
                  'year_built', 'structure_tax_value', 'tax_value', 'land_tax_value', 'tax_amount', 'census_id',
                  'log_error', 'transaction_date', 'bed_plus_bath', 'property_age', 'transaction_month'
             ]
    
    # Reordering Columns
    df = df[['index_id', 'parcel_id',
        'log_error', 'tax_value', 'structure_tax_value', 'land_tax_value', 'tax_amount',
        'county_id', 'zip_code', 'latitude', 'longitude', 'census_id',
        'bathrooms', 'bedrooms', 'full_bathrooms', 'bed_plus_bath', 'room_count',
        'property_sqft', 'lot_sqft',
        'land_use_code', 'land_use_type',
        'year_built', 'property_age', 'transaction_date', 'transaction_month'
       ]]
    
    return df

    ################################### Preprocess Zillow Data ########################################