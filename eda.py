import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from PIL import Image

def run():
    st.title('Bank Telemarketing Potential Leads Prediction')

    # Tampilkan gambar
    img = Image.open('telemarketing.jpg')
    st.image(img, caption = 'Photo by: tonodiaz via Magnific')

    # load data
    data = pd.read_csv('bank-full.csv', sep=';')
    data = data.rename(columns={'y':'subscribe'})

    # show table
    st.write('### Dataset preview')
    preview = data.head(100)
    st.dataframe(preview)

    # buat pie chart
    st.write('### Contact Method Distribution')
    contact_counts = data['contact'].value_counts().reset_index()
    contact_counts.columns = ['contact', 'count']

    fig = px.pie(
    contact_counts,
    values='count',
    names='contact',
    title='Contact Method Distribution',
    hole=0.4)
    st.plotly_chart(fig)

    # fig, ax = plt.subplots(figsize=(12,8))
    # data['contact'].value_counts().plot(kind='pie', autopct="%.2f%%", ax=ax)
    # st.pyplot(fig)

    # buat table 
    st.write('### Pekerjaan nasabah yang paling banyak convert')
    subs = data[data['subscribe'] == 'yes']['job'].value_counts().reset_index()
    subs = subs.sort_values(by='count', ascending=False).head()
    st.table(subs)

    # buat histogram
    st.write('### Histogram berdasarkan user input')
    option = st.selectbox('Pilih kolom untuk histogram:', ['age', 'balance'])
    fig = plt.figure(figsize=(12,8))
    sns.histplot(data[option], bins=20, kde = True)
    st.pyplot(fig)

    # buat plotly
    st.write('### Scatterplot dengan plotly')
    fig = px.scatter(data, x = 'age', y = 'balance', hover_data = ['age', 'balance'])
    st.plotly_chart(fig)

if __name__ == '__main__':
    run()