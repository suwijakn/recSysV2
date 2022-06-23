import streamlit as st
import pandas as pd

pd.options.display.float_format = "{:,.2f}".format
st.title('Select Product')

#df_img = pd.read_csv("/Users/suwijakn/Desktop/Swoop Buddy/New/june-21-2022-product_img.csv") 
#df_sim = pd.read_csv("/Users/suwijakn/Desktop/Swoop Buddy/New/simMatrix_june-22-2022.csv") 

url = 'https://raw.githubusercontent.com/suwijakn/recSysV2/main/june-21-2022-product_img.csv'
#df = pd.read_csv(url, index_col=0)
df_img = pd.read_csv(url) 
url = 'https://raw.githubusercontent.com/suwijakn/recSysV2/main/simMatrix_june-22-2022.csv'
df_sim = pd.read_csv(url) 


option = st.selectbox('Select Product', df_sim['x'].unique())
st.title('You selected:', option)

col1, col2, col3 = st.columns([1,6,1])

with col1:
    st.write("")

with col2:
    url = 'https://swap-project-bucket.s3.amazonaws.com/' + df_img[df_img['sku']==option]['img_url'].values[0]
    st.image(
            url,
            width=300, # Manually Adjust the width of the image as per requirement
        )
with col3:
    st.write("")

st.title('Similar Items')
df_sim[(df_sim['x'] == option)].sort_values('sim', ascending=False)['sku'].head()
#st.write(df_sim[(df_sim['x'] == option)].sort_values('sim', ascending=False)[['sku','sim']].head(5))

list_rec = df_sim[(df_sim['x'] == option)].sort_values('sim', ascending=False)['sku'].values[0:5]
list_sim = df_sim[(df_sim['x'] == option)].sort_values('sim', ascending=False)['sim'].values[0:5]
col1, col2, col3,col4, col5 = st.columns(5)

with col1:
    url = 'https://swap-project-bucket.s3.amazonaws.com/' + df_img[df_img['sku']==list_rec[0]]['img_url'].values[0]
    st.image(
            url,
            width=150, # Manually Adjust the width of the image as per requirement
        )
    st.write(list_rec[0])
    st.write('score = ' + str(list_sim[0])[0:5])

with col2:
    url = 'https://swap-project-bucket.s3.amazonaws.com/' + df_img[df_img['sku']==list_rec[1]]['img_url'].values[0]
    st.image(
            url,
            width=150, # Manually Adjust the width of the image as per requirement
        )
    st.write(list_rec[1])
    st.write('score = ' + str(list_sim[1])[0:5])
with col3:
    url = 'https://swap-project-bucket.s3.amazonaws.com/' + df_img[df_img['sku']==list_rec[2]]['img_url'].values[0]
    st.image(
            url,
            width=150, # Manually Adjust the width of the image as per requirement
        )
    st.write(list_rec[2])
    st.write('score = ' + str(list_sim[2])[0:5])
with col4:
    url = 'https://swap-project-bucket.s3.amazonaws.com/' + df_img[df_img['sku']==list_rec[3]]['img_url'].values[0]
    st.image(
            url,
            width=150, # Manually Adjust the width of the image as per requirement
        )
    st.write(list_rec[3])
    st.write('score = ' + str(list_sim[3])[0:5])
with col5:
    url = 'https://swap-project-bucket.s3.amazonaws.com/' + df_img[df_img['sku']==list_rec[4]]['img_url'].values[0]
    st.image(
            url,
            width=150, # Manually Adjust the width of the image as per requirement
        )
    st.write(list_rec[4])
    st.write('score = ' + str(list_sim[4])[0:5])