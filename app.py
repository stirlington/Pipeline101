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
        'Candidates': [{'Name': '', 'Salary': 0, 'Currency': 'GBP'}],
        'Fee %': 0,
        'Fee (£)': 0,
        'Probability %': 0,
        'Probability Fee (£)': 0,
        'VAT': 'Yes',
        'Est. Invoice Month': '',
        'Est. Invoice Year': ''
    })

# Display the pipeline table
def display_pipeline():
    st.title("Perm Pipeline")
    
    # Add new row button
    if st.button("Add New Row"):
        add_row()
    
    # Display each row in the pipeline data
    for i, row in enumerate(st.session_state.pipeline_data):
        st.write(f"### Vacancy {i+1}")
        
        # Consultant and client details
        col1, col2, col3 = st.columns([1, 2, 2])
        
        with col1:
            row['Consultant'] = st.selectbox(f"Consultant {i+1}", ['Chris', 'Max'], index=['Chris', 'Max'].index(row['Consultant']), key=f"consultant_{i}")
            row['Client Name'] = st.text_input(f"Client Name {i+1}", value=row['Client Name'], key=f"client_name_{i}")
            row['Role'] = st.text_input(f"Role {i+1}", value=row['Role'], key=f"role_{i}")
        
        with col2:
            for j, candidate in enumerate(row['Candidates']):
                candidate['Name'] = st.text_input(f"Candidate {j+1} Name", value=candidate['Name'], key=f"candidate_name_{i}_{j}")
                candidate['Salary'] = st.number_input(f"Candidate {j+1} Salary", value=candidate['Salary'], key=f"candidate_salary_{i}_{j}")
                candidate['Currency'] = st.selectbox(f"Candidate {j+1} Currency", ['GBP', 'USD', 'EUR'], index=['GBP', 'USD', 'EUR'].index(candidate['Currency']), key=f"candidate_currency_{i}_{j}")

                # Fee and probability calculations for each candidate
                row['Fee %'] = st.number_input(f"Fee % for Candidate {j+1}", value=row['Fee %'], key=f"fee_percent_{i}_{j}")
                row['Probability %'] = st.number_input(f"Probability % for Candidate {j+1}", value=row['Probability %'], key=f"probability_{i}_{j}")

                # Calculate fees based on inputs
                fee, probability_fee = calculate_fees(candidate['Salary'], candidate['Currency'], row['Fee %'], row['Probability %'])
                candidate['Fee (£)'] = fee
                candidate['Probability Fee (£)'] = probability_fee

                # Display calculated fees
                st.write(f"Fee (£) for Candidate {j+1}: £{candidate['Fee (£)']:.2f}")
                st.write(f"Probability Fee (£) for Candidate {j+1}: £{candidate['Probability Fee (£)']:.2f}")

            # Add button to add another candidate to the same vacancy
            if st.button("Add Candidate", key=f"add_candidate_{i}"):
                row['Candidates'].append({'Name': '', 'Salary': 0, 'Currency': 'GBP'})

        with col3:
            # VAT and estimated invoice date for the vacancy
            row['VAT'] = st.selectbox(f"VAT for Vacancy {i+1}", ['Yes', 'No'], index=['Yes', 'No'].index(row['VAT']), key=f"vat_{i}")
            row['Est. Invoice Month'] = st.selectbox(f"Est. Invoice Month for Vacancy {i+1}", ['January', 'February', 
                                                                                                'March', 
                                                                                                'April', 
                                                                                                'May', 
                                                                                                'June', 
                                                                                                'July', 
                                                                                                'August', 
                                                                                                'September', 
                                                                                                'October', 
                                                                                                'November', 
                                                                                                'December'], key=f"invoice_month_{i}")
            current_year = pd.Timestamp.now().year
            row['Est. Invoice Year'] = st.selectbox(f"Est. Invoice Year for Vacancy {i+1}", [current_year, current_year + 1, current_year + 2], key=f"invoice_year_{i}")

            # Action buttons
            if st.button("Move to Offered", key=f"move_offered_{i}"):
                # Logic to move to offered list (not implemented)
                st.success(f"Moved {row['Candidates'][0]['Name']} to Offered")

            if st.button("Delete", key=f"delete_{i}"):
                del st.session_state.pipeline_data[i]
                st.experimental_rerun()

# Run the pipeline display function to render the page
display_pipeline()
