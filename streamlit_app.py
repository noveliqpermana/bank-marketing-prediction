import streamlit as st
import eda
import prediction
from utils import cardinality

page = st.sidebar.selectbox('Tampilkan Page: ', ['EDA', 'Prediction'])

if page == 'EDA':
    eda.run()
    
else:
    prediction.run()