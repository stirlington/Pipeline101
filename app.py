import streamlit as st
import pandas as pd
from PIL import Image

# Load logo
logo = Image.open("logo.png")

# Display logo and title
st.image(logo, width=150)
st.title("Recruitment Pipeline Tracker")

# Initialize session state for data storage
if 'pipeline_data' not in st.session_state:
    st.session_state['pipeline_data'] = []
if 'offered_list' not in st.session_state:
    st.session_state['offered_list'] = []

# Function to load data into DataFrame
def load_data(data_key):
    return pd.DataFrame(st.session_state[data_key])

# Function to add candidate to pipeline
def add_to_pipeline():
    new_entry = {
        'Consultant': st.selectbox('Consultant', ['Chris', 'Max']),
        'Client Name': st.text_input('Client Name'),
        'Role': st.text_input('Role'),
        'Candidate': st.text_input('Candidate'),
        'Salary/Rate': st.number_input('Salary/Rate', min_value=0.0),
        'Fee %': st.number_input('Fee %', min_value=0.0),
        'Fee (£)': st.number_input('Fee (£)', min_value=0.0),
        'Probability %': st.number_input('Probability %', min_value=0.0),
        'Probability Fee (£)': st.number_input('Probability Fee (£)', min_value=0.0),
        'VAT': st.selectbox('VAT', ['Yes', 'No']),
        'Est Invoice Month': st.selectbox('Est Invoice Month', ['January', 'February', 'March', 
                                                                'April', 'May', 'June', 
                                                                'July', 'August', 'September', 
                                                                'October', 'November', 'December'])
    }
    if st.button('Add to Pipeline'):
        st.session_state['pipeline_data'].append(new_entry)
        st.success("Candidate added to pipeline!")

# Function to move candidate to offered list
def move_to_offered(index):
    offered_candidate = st.session_state['pipeline_data'].pop(index)
    st.session_state['offered_list'].append(offered_candidate)
    st.success("Candidate moved to offered list!")

# Display pipeline candidates
st.header("Pipeline Candidates")
pipeline_df = load_data('pipeline_data')
st.dataframe(pipeline_df)

for i, row in pipeline_df.iterrows():
    if st.button(f"Move {row['Candidate']} to Offered", key=f"offer_{i}"):
        move_to_offered(i)

# Display offered candidates
st.header("Offered Candidates")
offered_df = load_data('offered_list')
st.dataframe(offered_df)

# Add new candidate section
st.header("Add New Candidate to Pipeline")
add_to_pipeline()
