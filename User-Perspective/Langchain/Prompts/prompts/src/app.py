import streamlit as st 

st.write("kese ho bhai tum")
st.title("ye hai title")
st.header("ye hai header")
st.markdown("""
            # this is markdown stuff 
            ## thsi sis h2 stuff 
            - l1 
            - l2
            - l3
            """)
st.caption("Book")

st.code("""
st.write("kese ho bhai tum")
st.title("ye hai title")
st.header("ye hai header")
st.markdown(\"\"\" # yaha tum triple quotes direct  use nahi  kar sakte hai because python hai ye 
# this is markdown stuff 
## this is h2 stuff 
- l1 
- l2
- l3
\"\"\")
st.caption("Book")
""")

name = st.text_input("Name",placeholder="Enter you name")
st.write("user name :",name)
import datetime
st.date_input(label="Your DOB" , max_value=datetime.date.today())

user_c = st.chat_input("Likh be ...")
st.write(user_c)

st.text_area("message ")


age = st.slider("Your age" ,min_value=18 ,max_value=20)
st.write(age )

genders = ["male","female","other"]
st.radio("Your gender",options=genders)
# lly checkbox and all that stuff 

# file upload 
up_f = st.file_uploader("choose a file",type=['csv,tsv'])