import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
def load_data():
    df=pd.read_csv('Bank Customer Churn Prediction.csv')
    return df
df=load_data()
def exploratory_page():
    st.title(' CUSTOMER CHURN DATASET')
    st.write('### DASHBOARD SHOWING CUSTOMER CHURN FOR ABC BANK')

    st.write("""#### NUMBER OF DATA FROM DIFFERENT COUNTRIES""")
    data=df['country'].value_counts()
    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal")
    st.pyplot(fig1) 

    st.write("""#### NUMBER OF GENDER""")
    data=df['gender'].value_counts()
    fig2, ax2 = plt.subplots()
    ax2.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    ax2.axis("equal")
    st.pyplot(fig2) 

    st.write('### COUNT OF CHURN')
    fig3=plt.figure(figsize=(10,7))
    sns.countplot(x='churn',palette='Set2',data=df)
    st.pyplot(fig3)



    
    

    st.write('### DISTRIBUTION OF ESTIMATED SALARY')
    fig4=plt.figure(figsize=(10,7))
    sns.histplot(x=df['estimated_salary'],kde=True)
    st.pyplot(fig4)

    st.write('### DISTRIBUTION OF AGE')
    fig5=plt.figure(figsize=(10,7))
    sns.histplot(x=df['age'],kde=True)
    st.pyplot(fig5)

    st.write('### DISTRIBUTION OF BALANCE')
    fig6=plt.figure(figsize=(10,7))
    sns.histplot(x=df['balance'],kde=True)
    st.pyplot(fig6)

    st.write('### DISTRIBUTION OF CREDIT SCORE')
    fig7=plt.figure(figsize=(10,7))
    sns.histplot(x=df['credit_score'],kde=True)
    st.pyplot(fig7)















