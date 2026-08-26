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
    multi = """
    Pelaksanaan direct marketing campaign yang dilakukan oleh bank seringkali memakan banyak biaya dan effort tim marketing dan telemarketing. Hal ini biasa disebabkan oleh kurangnya pre-screening sebelum campaign dieksekusi sehingga banyak leads atau nasabah yang sebetulnya tidak tertarik juga menjadi target dalam campaign tersebut.

    Banyak institusi bank mengalami kesulitan dalam mengidentifikasi leads yang memiliki potensi tinggi untuk menerima tawaran deposit berjangka (term deposit) sehingga menyebabkan cost marketing yang tinggi dan juga conversion yang rendah.

    Maka dari itu model prediksi ini dibuat untuk membantu tim marketing dalam menentukan profil nasabah mana yang bisa dihubungi lebih lanjut untuk ditawarkan produk deposit berjangka. Project ini bertujuan untuk mencari model algoritma classification terbaik dengan melakukan percobaan ke berbagai jenis algoritma seperti KNN, SVM, Decision Tree, Random Forest dan XGBoost.
    """
    st.markdown(multi)

    # load data
    data = pd.read_csv('bank-full.csv', sep=';')
    data = data.rename(columns={'y':'subscribe'})

    # show table
    st.write('## Dataset overview')
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