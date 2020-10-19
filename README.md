# Predicting Home Values for Zillow
## About the Project
### Goals
When someone wants to know the value of a property, our website is often one of the top recommendations. However, there is always room for improvement, and I want to accomplish this improvement with clustering methodologies to determine where error may be coming from.  

How can we improve? By creating a model to predict log error in our current Zestimate, we can determine what is driving this error.
### Background
### Outline

<img src="https://i.pinimg.com/originals/d9/1e/c8/d91ec86bd333b492345ce6bf8b323bbf.png" width="250" height="420" /> 

### Data Dictionary
The linked Data Quality [Report](https://drive.google.com/file/d/1wh3iKkAX7o-PZ46EcsHzoZbxtD-BKB6-/view)
reviews the raw aquired data from the zillow database. It includes next steps for each feature, such as dropping the feature or preparing for modeling. The data dictionary below will include the columns used or created after prepping this data.  
![Data-Dictionary](https://i.pinimg.com/originals/21/12/10/211210b304ce26a7f87bd770fefb7c7e.png)
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
## Explore
## Model
## Conclusion
# How to Reproduce
- [x] Read this README.md
- [ ] Download Acquire.py, Prepare.py, and Final_Model.ipynb in your working directory.
    - Click [here](https://drive.google.com/file/d/1NMZyc3-N4zakq82ZDAZjeYl0BVAEoBhR/view) for a reference to the module functions.
- [ ] Run the Final_Modeling.ipynb Jupyter Notebook.
- [ ] Do your own exploring, modeling, etc.
# Author
![Home-Sale-Sign](https://i.pinimg.com/564x/68/de/23/68de2379e0fec17a991ab4c1ab588c46.jpg)
