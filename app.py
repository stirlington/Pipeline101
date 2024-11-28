import streamlit as st
import pandas as pd

# Initialize session state for pipeline data
if 'pipeline_data' not in st.session_state:
    st.session_state.pipeline_data = pd.DataFrame(columns=[
        'Consultant', 'Client Name', 'Vacancy', 'Candidate', 'Salary/Hourly Rate',
        'Currency', 'Fee %', 'Fee £', 'Probability %', 'Probability £',
        'VAT', 'Estimated Month'
    ])

# Function to display the logo at the top left
def display_logo():
    st.image("logo.png", width=100)

def pipeline_page():
    display_logo()
    st.title("Pipeline")

    # Add new row button
    if st.button("Add New Row"):
        new_row = pd.Series({
            'Consultant': '',
            'Client Name': '',
            'Vacancy': '',
            'Candidate': '',
            'Salary/Hourly Rate': 0.0,
            'Currency': '',
            'Fee %': 0.0,
            'Fee £': 0.0,
            'Probability %': 0.0,
            'Probability £': 0.0,
            'VAT': '',
            'Estimated Month': ''
        })
        st.session_state.pipeline_data = st.session_state.pipeline_data.append(new_row, ignore_index=True)

    # Display and edit table
    for index, row in st.session_state.pipeline_data.iterrows():
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            consultant = st.selectbox('Consultant', ['Chris', 'Max'], key=f'consultant_{index}')
        with col2:
            client_name = st.text_input('Client Name', row['Client Name'], key=f'client_{index}')
        with col3:
            vacancy = st.text_input('Vacancy', row['Vacancy'], key=f'vacancy_{index}')
        with col4:
            candidate = st.text_input('Candidate', row['Candidate'], key=f'candidate_{index}')
        with col5:
            salary_hourly_rate = st.number_input('Salary/Hourly Rate', value=row['Salary/Hourly Rate'], key=f'salary_{index}')

        fee_percent = st.number_input('Fee %', value=row['Fee %'], key=f'fee_percent_{index}')
        probability_percent = st.number_input('Probability %', value=row['Probability %'], key=f'probability_percent_{index}')
        
        currency = st.selectbox('Currency', ['£', '$', '€'], key=f'currency_{index}')
        vat = st.selectbox('VAT Applicable?', ['Yes', 'No'], key=f'vat_{index}')
        
        estimated_month = st.selectbox('Estimated Month of Projection',
                                       ["January", "February", "March", "April", "May", "June",
                                        "July", "August", "September", "October", "November", "December"],
                                       key=f'estimated_month_{index}')

        # Calculate Fee £ and Probability £ automatically
        fee_pounds = salary_hourly_rate * (fee_percent / 100)
        probability_pounds = fee_pounds * (probability_percent / 100)

        # Update session state
        st.session_state.pipeline_data.at[index, :] = [
            consultant, client_name, vacancy, candidate, salary_hourly_rate,
            currency, fee_percent, fee_pounds, probability_percent,
            probability_pounds, vat, estimated_month
        ]

    # Display the updated DataFrame
    st.dataframe(st.session_state.pipeline_data)

def main():
    pages = {
        "Pipeline": pipeline_page,
    }
    
    # Sidebar navigation
    selection = st.sidebar.radio("Go to", list(pages.keys()))
    
    page_function = pages[selection]
    
    page_function()

if __name__ == "__main__":
    main()
