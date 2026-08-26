import streamlit as st
import pickle
import json
import pandas as pd
import numpy as np
from utils import cardinality

# load semua file yang dibutuhkan
with open('pipeline.pkl', 'rb') as file:
    pipeline = pickle.load(file)

def run():
    with st.form('prediction form'):
        age = st.number_input('Age: ', min_value = 17, max_value = 100, value = 20)
        job = st.selectbox('Job: ', ['management', 'technician', 'entrepreneur', 'blue-collar', 'unknown', 'retired', 'admin.', 'services', 'self-employed', 'unemployed', 'housemaid', 'student'], index = 4)	
        marital = st.selectbox('Marital status: ', ['married', 'single', 'divorced'], index = 1)
        education = st.selectbox('Education level: ', ['tertiary', 'secondary', 'unknown', 'primary'], index = 2)
        default = st.selectbox("Has credit card: ", ['yes', 'no'], index = 1)	
        balance = st.number_input('Balance: ', min_value = -5000, max_value = 999999, value = 0)
        housing = st.selectbox("Has housing loan: ", ['yes', 'no'], index = 1)
        loan = st.selectbox("Has personal loan: ", ['yes', 'no'], index = 1)
        contact = st.selectbox('Contact method: ', ['unknown', 'cellular', 'telephone'], index = 1)
        day = st.number_input('Date - day: ', min_value = 1, max_value = 31, value = 1)
        month = st.selectbox('Date - month: ', ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'], index = 0)
        campaign = st.number_input('Contact made during this campaign: ', min_value = 0, max_value = 100, value = 0)
        pdays = st.number_input('Days passed after last contact: ', min_value = -1, max_value = 850, value = 0)
        previous = st.number_input('Contact made during previous campaigns: ', min_value = 0, max_value = 100, value = 0)
        poutcome = st.selectbox('Previous outcome: ', ['unknown', 'failure', 'other', 'success'], index = 0)

        submitted = st.form_submit_button('Predict')

    data_inf = {
        'age': age,
        'job': job,	
        'marital': marital,	
        'education': education,	
        'default': default,	
        'balance': balance,
        'housing': housing,
        'loan': loan,
        'contact': contact,
        'day': day,
        'month': month,
        'campaign': campaign,
        'pdays': pdays,
        'previous': previous,
        'poutcome': poutcome
    }

    data_inf = pd.DataFrame([data_inf])

    st.dataframe(data_inf)

    if submitted:
        # predict y
        y_pred_inf = pipeline.predict(data_inf)
        y_proba_inf = pipeline.predict_proba(data_inf)[:,1]

        result = data_inf.copy()
        result['prediction'] = y_pred_inf
        result['prediction_label'] = result['prediction'].map({0:'Will not subscribe', 1:'Will subscribe'})
        result['probability'] = y_proba_inf.round(3)

        st.write('## Rating: ', (result['prediction_label'][0]))

        st.write('### Table Result')
        st.dataframe(result)

if __name__ == "__main__":
  run()