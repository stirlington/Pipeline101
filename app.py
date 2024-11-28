import streamlit as st
import pandas as pd

# Initialize session state for pipeline data
if 'pipeline_data' not in st.session_state:
    st.session_state.pipeline_data = pd.DataFrame(columns=[
        'Consultant', 'Client Name', 'Role', 'Candidate', 'Salary/Hourly Rate',
        'Currency', 'Fee %', 'Fee (£)', 'Probability %', 'Probability Fee (£)',
        'VAT', 'Est. Invoice Month', 'Year'
    ])

# Function to display the logo at the top left
def display_logo():
    st.image("logo.png", width=100)

def pipeline_page():
    display_logo()
    st.title("Perm Pipeline")

    # Add new row button
    if st.button("Add New Row"):
        new_row = pd.Series({
            'Consultant': 'Chris',
            'Client Name': '',
            'Role': '',
            'Candidate': '',
            'Salary/Hourly Rate': 0.0,
            'Currency': 'USD',
            'Fee %': 20.0,
            'Fee (£)': 0.0,
            'Probability %': 100.0,
            'Probability Fee (£)': 0.0,
            'VAT': '',
            'Est. Invoice Month': '',
            'Year': 2024
        })
        st.session_state.pipeline_data = st.session_state.pipeline_data.append(new_row, ignore_index=True)

    # Display and edit table
    for index, row in st.session_state.pipeline_data.iterrows():
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            consultant = st.selectbox('Consultant', ['Chris', 'Max'], index=['Chris', 'Max'].index(row['Consultant']), key=f'consultant_{index}')
        with col2:
            client_name = st.text_input('Client Name', row['Client Name'], key=f'client_{index}')
        with col3:
            role = st.text_input('Role', row['Role'], key=f'role_{index}')
        with col4:
            candidate = st.text_input('Candidate', row['Candidate'], key=f'candidate_{index}')
        with col5:
            salary_hourly_rate = st.number_input('Salary/Hourly Rate', value=row['Salary/Hourly Rate'], key=f'salary_{index}')

        currency = st.selectbox('Currency', ['£', '$', '€'], index=['£', '$', '€'].index(row['Currency']), key=f'currency_{index}')
        fee_percent = st.number_input('Fee %', value=row['Fee %'], key=f'fee_percent_{index}')
        probability_percent = st.number_input('Probability %', value=row['Probability %'], key=f'probability_percent_{index}')
        
        vat = st.selectbox('VAT Applicable?', ['Yes', 'No'], index=['Yes', 'No'].index(row['VAT']), key=f'vat_{index}')
        
        est_invoice_month = st.selectbox('Est. Invoice Month',
                                         ["January", "February", "March", "April", "May", "June",
                                          "July", "August", "September", "October", "November", "December"],
                                         index=["January", "February", "March", "April", "May", "June",
                                                "July", "August", "September", "October", "November", "December"].index(row['Est. Invoice Month']),
                                         key=f'estimated_month_{index}')
        
        year = st.selectbox('Year', [2024, 2025, 2026], index=[2024, 2025, 2026].index(row['Year']), key=f'year_{index}')

        # Calculate Fee £ and Probability Fee £ automatically
        fee_pounds = salary_hourly_rate * (fee_percent / 100)
        probability_fee_pounds = fee_pounds * (probability_percent / 100)

        # Update session state
        st.session_state.pipeline_data.at[index, :] = [
            consultant, client_name, role, candidate, salary_hourly_rate,
            currency, fee_percent, fee_pounds, probability_percent,
            probability_fee_pounds, vat, est_invoice_month, year
        ]

        # Action buttons
        move_col1, move_col2 = st.columns(2)
        
        with move_col1:
            if st.button("Move to Offered", key=f'move_offered_{index}'):
                # Logic to move to offered (not implemented)
                pass
        
        with move_col2:
            if st.button("Delete", key=f'delete_{index}'):
                # Logic to delete the row
                st.session_state.pipeline_data.drop(index, inplace=True)

    # Display the updated DataFrame
    st.dataframe(st.session_state.pipeline_data)

def main():
    pages = {
        "Home": lambda: None,
        "Perm Pipeline": pipeline_page,
        "Contractor Pipeline": lambda: None,
        "Perm Offers": lambda: None,
        "Contractor Offers": lambda: None,
        "Rejected/Failed": lambda: None,
        "Invoiced": lambda: None,
        "Stats": lambda: None,
    }
    
    # Sidebar navigation
    selection = st.sidebar.radio("Go to", list(pages.keys()))
    
    page_function = pages[selection]
    
    page_function()

if __name__ == "__main__":
    main()
