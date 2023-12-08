# pip install -U streamlit
# pip install -U plotly
#!pip install -U sklearn
#!pip install -U scikit-learn

import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install(sklearn)
install(scikit-learn)

# you can run your app with: streamlit run app.py

import streamlit as st
import pickle

# loading the trained model
model = pickle.load(open('model.pkl', 'rb'))

# create title
st.title('Predicting if message is spam or not')

message = st.text_input('Enter a message')

submit = st.button('Predict')

if submit:
    prediction = model.predict([message])

    # print(prediction)
    # st.write(prediction)
    
    if prediction[0] == 'spam':
        st.warning('This message is spam')
    else:
        st.success('This message is Legit (HAM)')


st.balloons()
