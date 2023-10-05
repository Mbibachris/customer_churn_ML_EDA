import streamlit as st
from PREDICTION import prediction
from customerEXPLORE import exploratory_page

page=st.selectbox('DO YOU WANT TO EXPLORE OR PREDICT',('EXPLORE','PREDICT'))

if page=='EXPLORE':
    exploratory_page()
    st.divider()
    st.title(" CONCLUSION")
    st.write('''The categorical variables were well distributed with just a few differences in the counts of the various classes in the variables with the exception of product number which had classes that were hugely under represented.The continous variables were all normally distributed with the exception of the estimated salary that had a seemly uniform distribution. However, there were a few outliers in the age and balance variables which may not impact the modelling significantly. In terms of comparing churn to all other categorical variables the number of customers staying was significantly more than those leaving.''')
else:
    prediction()

