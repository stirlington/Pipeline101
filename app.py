import streamlit as st
import pandas as pd
import numpy as np

# Initialize sample data
pipeline_data = pd.DataFrame(columns=[
    'Consultant', 'Client Name', 'Vacancy', 'Candidate', 'Salary/Hourly Rate',
    'Currency', 'Fee %', 'Fee £', 'Probability %', 'Probability £',
    'VAT', 'Estimated Month'
])

# Function to display the logo at the top left
def display_logo():
    st.image("logo.png", width=100)

def home_page():
    display_logo()
    st.title("Home Page")
    
    # Dropdown for selecting year
    year = st.selectbox("Select Year", ["2024", "2025", "2026"])
    
    # Table for projected amounts by month
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    projected_amounts = {month: np.random.randint(1000, 10000) for month in months}
    
    # Create a DataFrame for display
    df_projected = pd.DataFrame(list(projected_amounts.items()), columns=["Month", f"Projected Amount (£) for {year}"])
    
    # Display the DataFrame
    st.table(df_projected)

def pipeline_page():
    display_logo()
    st.title("Pipeline")
    
    global pipeline_data
    
    # Editable DataFrame for pipeline with dropdowns and auto-calculation
    if st.button("Add Candidate"):
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
        pipeline_data = pipeline_data.append(new_row, ignore_index=True)

    edited_pipeline_data = pipeline_data.copy()

    for index, row in edited_pipeline_data.iterrows():
        consultant = st.selectbox('Consultant', ['Chris', 'Max'], key=f'consultant_{index}')
        client_name = st.text_input('Client Name', row['Client Name'], key=f'client_{index}')
        vacancy = st.text_input('Vacancy', row['Vacancy'], key=f'vacancy_{index}')
        candidate = st.text_input('Candidate', row['Candidate'], key=f'candidate_{index}')
        salary_hourly_rate = st.number_input('Salary/Hourly Rate', value=row['Salary/Hourly Rate'], key=f'salary_{index}')
        currency = st.selectbox('Currency', ['£', '$', '€'], key=f'currency_{index}')
        fee_percent = st.number_input('Fee %', value=row['Fee %'], key=f'fee_percent_{index}')
        probability_percent = st.number_input('Probability %', value=row['Probability %'], key=f'probability_percent_{index}')
        vat = st.selectbox('VAT Applicable?', ['Yes', 'No'], key=f'vat_{index}')
        estimated_month = st.selectbox('Estimated Month of Projection', months, key=f'estimated_month_{index}')

        fee_pounds = salary_hourly_rate * (fee_percent / 100)
        probability_pounds = fee_pounds * (probability_percent / 100)

        edited_pipeline_data.at[index, :] = [consultant, client_name, vacancy, candidate, salary_hourly_rate,
                                             currency, fee_percent, fee_pounds, probability_percent,
                                             probability_pounds, vat, estimated_month]

    if not edited_pipeline_data.equals(pipeline_data):
        pipeline_data.update(edited_pipeline_data)
        st.success('Pipeline updated successfully!')

def offered_pipeline():
    display_logo()
    st.title("Offered Pipeline")
    
def invoice_pipeline():
    display_logo()
    st.title("Invoice Pipeline")
    
def rejected_pipeline():
    display_logo()
    st.title("Rejected Pipeline")

def stats_page():
    display_logo()
    st.title("Stats Page")

def main():
    pages = {
        "Home": home_page,
        "Pipeline": pipeline_page,
        "Offered": offered_pipeline,
        "Invoice": invoice_pipeline,
        "Rejected": rejected_pipeline,
        "Stats": stats_page,
    }
    
    # Set page config and theme
    primary_color = "#80CE78"
    
    # Apply sidebar styling using primary color
    sidebar_style = f"""
        <style>
            .css-1d391kg {{
                background-color: {primary_color};
            }}
            .css-18e3th9 {{
                padding-top: 50px;
            }}
            .css-1aumxhk {{
                padding-left: 10px;
            }}
        </style>
        """
    
    # Apply sidebar styling
    st.markdown(sidebar_style, unsafe_allow_html=True)

    # Sidebar navigation
    selection = st.sidebar.radio("Go to", list(pages.keys()))
    
    page_function = pages[selection]
    
    page_function()

if __name__ == "__main__":
    main()
