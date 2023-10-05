import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
#loading model
def load_model():
    with open('CustomerChurn.pk1','rb') as file:
        data=pickle.load(file)
        return data
data= load_model()
model=data['model']
scaler=data['scaler']

# BUILDING THE PAGE

def prediction():
    st.title('BANK CUSTOMER CHURN PREDICTION')
    st.write('### The following information is needed to predict the customer churn')
    COUNTRY=('France','Germany','Spain')
    Gender=('Male','Female')
    HasCrCard = ("Yes", "No")
    IsActiveMember = ("Yes", "No")

    CreditScore=st.number_input('ENTER CUSTOMER CREDIT SCORE')
    Age=st.number_input('ENTER CUSTOMER AGE')
    Tenure=int(st.slider('HOW LONG HAVE YOU BEEN WITH THE BANK',1,10,2))
    Balance=st.number_input('WHAT IS CUSTOMER ACCOUNT BALANCE')
    NOP=int(st.slider('WHAT IS THE NUMBER PRODUCT CUSTOMER HAVE PURCHASED FROM THE BANK',1,10,2))
    hasCreditCard=st.radio('DOES CUSTOMER HAVE A CREDIT CARD',HasCrCard)
    isActiveMember=st.radio('IS CUSTOMER ACTIVE',IsActiveMember)
    geography_any=st.selectbox('WHICH COUNTRY IS CUSTOMER FROM',COUNTRY)
    gender_any=st.radio('WHAT IS CUSTOMER GENDER',Gender)
    salary=st.number_input('WHAT IS CUSTOMER ESTIMATED SALARY')

    for item in HasCrCard:
        if item == hasCreditCard:
            hasCreditCard = 1
        elif item == hasCreditCard:
            hasCreditCard = 0

    for item in IsActiveMember:
        if item == isActiveMember:
            isActiveMember = 1
        elif item == isActiveMember:
            isActiveMember = 0

    Geography_France, Geography_Germany, Geography_Spain = None, None, None
    if geography_any == "France":
        Geography_France = 1
        Geography_Germany = 0
        Geography_Spain = 0
    elif geography_any == "Germany":
        Geography_France = 0
        Geography_Germany = 1
        Geography_Spain = 0
    else:
        Geography_France = 0
        Geography_Germany = 0
        Geography_Spain = 1

    
    Gender_Female, Gender_Male = None, None
    if gender_any == "Female":
        Gender_Female = 1
        Gender_Male = 0
    else:
        Gender_Female = 0
        Gender_Male = 1

    st.divider()
    button_pressed = st.button("Predict!", help="Click to make prediction")

    if button_pressed:
        estimator = np.array(
            [
                [
                    CreditScore,
                    Age,
                    Tenure,
                    Balance,
                    NOP,
                    hasCreditCard,
                    isActiveMember,
                    salary,
                    Geography_France,
                    Geography_Germany,
                    Geography_Spain,
                    Gender_Female,
                    Gender_Male,
                    
                ]
            ]
        )
        scaled_data = scaler.transform(estimator)
        result = model.predict(scaled_data)

        # if a successful prediction

        if result[0] == 1:
            message = "CUSTOMER LEFT THE BANK:thumbsdown:"
            st.subheader(message)
        else:
            message = "CUSTOMER DID NOT LEAVE THE BANK :thumbsup:"
            st.subheader(message)

    



