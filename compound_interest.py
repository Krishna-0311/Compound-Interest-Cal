import streamlit as st
from pathlib import Path
import pandas as pd

# from sklearn import datasets

# from sklearn.ensemble import RandomForestClassifier

from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
profile_pic = current_dir / "assets" / "profile-pic.jpg"



with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

Year_List=[2,3,4,5,6,7,8,9,10]

new_title = '<p style="font-family:sans-serif; color:#EFC050; font-size: 42px;">Compound Interest Calculator</p>'
st.markdown(new_title, unsafe_allow_html=True)





st.sidebar.header('User Input Values')



def user_input_features():

    Int_Rate = st.sidebar.slider('Interest Rate in %', 6.0, 42.0, 10.0)

    	##st.sidebar.add_rows

    Principal = st.sidebar.text_input('Please input Principal Amount',10000)

    	##st.sidebar.add_rows

    No_Of_Years = st.sidebar.selectbox('Select No Of Years',Year_List, 2)



    data = {'Int_Rate': Int_Rate,	
            'Principal': Principal,	
            'No_Of_Years': No_Of_Years}
    features = pd.DataFrame(data, index=[0])
    return features



df = user_input_features()

x = '<p style="font-family:sans-serif; color:#7FCDCD; font-size: 24px;">User Entered input for Rate, Principal amount and No.of years is</p>'
st.markdown(x,unsafe_allow_html=True)



st.write(df)


# Compound Interest function
def compound_int(Principal, Int_Rate, No_Of_Years):

    comp=1.0
    for i in range(0, int(No_Of_Years)):
        comp=comp*(1+Int_Rate/100)
        #st.write(comp)
    comp=float(Principal)*(comp-1)
    comp_text= str("Compound Interest is " + str("%.3f" % comp) )
    st.write(comp_text)
    data_1 = {'Computed_Compound_Interest': comp_text}

    result = pd.DataFrame(data_1, index=[0])

    return result

st.subheader('The calculated compound interest is: ')
df_1=compound_int(df.Principal, df.Int_Rate, df.No_Of_Years)







st.subheader('The Final CI is:')

st.write(df_1)

x = '<p style="font-family:sans-serif; color:#00CED1; font-size: 24px;">_______________________________________-deepu</p>'
st.markdown(x,unsafe_allow_html=True)
