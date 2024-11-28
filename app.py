import streamlit as st
import pandas as pd

# Initialize session state for storing pipeline data
if 'pipeline_data' not in st.session_state:
    st.session_state['pipeline_data'] = []

# Function to calculate fees
def calculate_fees(salary, currency, fee_percent, probability):
    conversion_rates = {'GBP': 1, 'USD': 0.79, 'EUR': 0.86}
    salary_in_gbp = salary * conversion_rates[currency]
    fee = (salary_in_gbp * fee_percent) / 100
    probability_fee = (fee * probability) / 100
    return fee, probability_fee

# Function to add a new row to the pipeline
def add_row():
    st.session_state.pipeline_data.append({
        'Consultant': 'Chris',
        'Client Name': '',
        'Role': '',
        'Candidate': '',
        'Salary': 0,
        'Currency': 'GBP',
        'Fee %': 0,
        'Fee (£)': 0,
        'Probability %': 0,
        'Probability Fee (£)': 0,
        'VAT': 'Yes',
        'Est. Invoice Month': '',
        'Est. Invoice Year': ''
    })

# Function to display the pipeline table
def display_pipeline():
    st.title("Perm Pipeline")
    
    # Add new row button
    if st.button("Add New Row"):
        add_row()
    
    # Display each row in the pipeline data
    for i, row in enumerate(st.session_state.pipeline_data):
        with st.expander(f"Row {i+1}"):
            row['Consultant'] = st.selectbox("Consultant", ['Chris', 'Max'], index=['Chris', 'Max'].index(row['Consultant']), key=f"consultant_{i}")
            row['Client Name'] = st.text_input("Client Name", value=row['Client Name'], key=f"client_name_{i}")
            row['Role'] = st.text_input("Role", value=row['Role'], key=f"role_{i}")
            row['Candidate'] = st.text_input("Candidate", value=row['Candidate'], key=f"candidate_{i}")
            row['Salary'] = st.number_input("Salary", value=row['Salary'], key=f"salary_{i}")
            row['Currency'] = st.selectbox("Currency", ['GBP', 'USD', 'EUR'], index=['GBP', 'USD', 'EUR'].index(row['Currency']), key=f"currency_{i}")
            row['Fee %'] = st.number_input("Fee %", value=row['Fee %'], key=f"fee_percent_{i}")
            row['Probability %'] = st.number_input("Probability %", value=row['Probability %'], key=f"probability_{i}")

            # Calculate fees based on inputs
            fee, probability_fee = calculate_fees(row['Salary'], row['Currency'], row['Fee %'], row['Probability %'])
            row['Fee (£)'] = fee
            row['Probability Fee (£)'] = probability_fee

            # Display calculated fees
            st.write(f"Fee (£): £{row['Fee (£)']:.2f}")
            st.write(f"Probability Fee (£): £{row['Probability Fee (£)']:.2f}")

            # VAT and estimated invoice date
            row['VAT'] = st.selectbox("VAT", ['Yes', 'No'], index=['Yes', 'No'].index(row['VAT']), key=f"vat_{i}")
            row['Est. Invoice Month'] = st.selectbox("Est. Invoice Month", ['January', 'February', 'March', 'April', 
                                                                          'May', 'June', 'July', 'August', 
                                                                          'September', 'October', 
                                                                          'November', 'December'], key=f"invoice_month_{i}")
            current_year = pd.Timestamp.now().year
            row['Est. Invoice Year'] = st.selectbox("Est. Invoice Year", [current_year, current_year + 1, current_year + 2], key=f"invoice_year_{i}")

            # Action buttons
            if st.button("Move to Offered", key=f"move_offered_{i}"):
                # Logic to move to offered list (not implemented)
                st.success(f"Moved {row['Candidate']} to Offered")

            if st.button("Delete", key=f"delete_{i}"):
                del st.session_state.pipeline_data[i]
                st.experimental_rerun()

# Run the pipeline display function to render the page
display_pipeline()
