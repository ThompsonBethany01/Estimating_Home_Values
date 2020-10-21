# Predicting Home Values for Zillow
## About the Project
### Goals
When someone wants to know the value of a property, our website is often one of the top recommendations. However, there is always room for improvement, and I want to accomplish this improvement with clustering methodologies to determine where error may be coming from. How can we improve? By creating a model to predict log error in our current Zestimate, we can determine what is driving this error.
### Background
According to the Zillow Kaggle competition,
> "By continually improving the median margin of error (from 14% at the onset to 5% today), Zillow has since become established as one of the largest, most 
> trusted marketplaces for real estate information in the U.S. and a leading example of impactful machine learning."  

````
                    The log error is defined as logerror=log(Zestimate)−log(SalePrice)
````
 
### Outline
The organization of this project is visualized below. Only Final_Model.ipynb and the .py files are necessary to reproduce. However, the module notebooks go more in-depth than the final notebook. Both the module notebooks and pdfs are additional resources about the project.

<img src="https://i.pinimg.com/originals/57/75/18/5775186c4bea7051bb0b701d41958434.png" /> 

### Data Dictionary
The linked Data Quality [Report](https://drive.google.com/file/d/1wh3iKkAX7o-PZ46EcsHzoZbxtD-BKB6-/view)
reviews the raw aquired data from the zillow database. It includes next steps for each feature, such as dropping the feature or preparing for modeling. The data dictionary below will include the columns used or created after prepping this data.  

<p align="center">
  <img src="https://i.pinimg.com/originals/21/12/10/211210b304ce26a7f87bd770fefb7c7e.png" width="800" height="500" >
</p> 

## Initial Thoughts & Hypothesis
### Thoughts
### Hypothesis
# Project Steps
## Acquire
Within the acquire.py module, there are functions to:
- connect to the SQL company database (login credentials required)
- read a query to select the data and save to a csv file
- assign the data to a variable
- count the nulls of each columns and calculate the percentage of this
## Prepare
The Prepare.py has two functions:  
To prepare
- contains the Acquire module to obtain data
- removes nulls in columns/rows
- removes outliers
- creates new columns
- rearranges/renames columns
- splits into train, validate, test  

To scale  
- drops log error and unscaleable columns (census/transaction date)
- creates standard scaler fit on train
- transforms on train, validate, and test
- returns the dataframes
## Explore
Once the data is split, explore on train to leave the rest of the data as *unseen*. Visualized independent features versus log error and clusters created in Tableau. Features and clusters were also checked for significance using hypothesis testing with T-test, Correlation test, and Anova test.  

Clusters created:  
- Tax using tax_value, tax_amount, tax_rate
- Square feet using property_sqft and lot_sqft
- Room/Age using full_bathrooms, bed_plus_bath, room_count, property_age
## Model
Baseline model was based on the average log error and had a RMSE score of 0.01421  
Final model chosen was a Polynomial Linear Regression with degree=3 on the top 9 features from SelectKBest.
- Train RMSE: 0.01416
- Validate RMSE: 0.21491
- Test RMSE: 0.31837
## Conclusion
Clusters and features explored did not have a significant difference with respect to log error. More exploration is needed to determine if other clusters can be created. Could these improve the model that predicts log error? Right now, the model's root mean squared error was about .1 higher than the baseline.
# How to Reproduce
- [x] Read this README.md
- [ ] Download Acquire.py, Prepare.py, Model.py, and Final_Model.ipynb in your working directory.
    - Click [here](https://drive.google.com/file/d/1NMZyc3-N4zakq82ZDAZjeYl0BVAEoBhR/view) for a reference to the module functions.
- [ ] Run the Final_Modeling.ipynb Jupyter Notebook.
- [ ] Do your own exploring, modeling, etc.
# Author
![Home-Sale-Sign](https://i.pinimg.com/564x/68/de/23/68de2379e0fec17a991ab4c1ab588c46.jpg)
