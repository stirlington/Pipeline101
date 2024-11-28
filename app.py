import streamlit as st
import pandas as pd
import numpy as np

# Initialize sample data
pipeline_data = pd.DataFrame(columns=[
    'Consultant', 'Client Name', 'Vacancy', 'Candidates', 'Currency',
    'Fee %', 'Fee £', 'Probability %', 'Probability £',
    'VAT', 'Estimated Month'
])

offered_data = pd.DataFrame(columns=pipeline_data.columns)
invoice_data = pd.DataFrame(columns=pipeline_data.columns)
rejected_data = pd.DataFrame(columns=pipeline_data.columns)

# Function to display the logo at the top left
def display_logo():
    st.sidebar.image("logo.png", use_column_width=True)

def home_page():
    display_logo()
    st.title("Home Page")
    
    year = st.selectbox("Select Year", ["2024", "2025", "2026"])
    month = st.selectbox("Select Month", [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ])
    
    st.write(f"Projected amount for {month} {year}: £{np.random.randint(1000, 10000)}")

def pipeline_page():
    display_logo()
    st.title("Pipeline")
    
    global pipeline_data
    
    # Editable DataFrame for pipeline
    edited_pipeline_data = st.experimental_data_editor(pipeline_data, num_rows="dynamic")
    
    if not edited_pipeline_data.equals(pipeline_data):
        pipeline_data = edited_pipeline_data.copy()
        st.success('Pipeline updated successfully!')
    
    # Adding multiple candidates to a single vacancy
    with st.form(key='add_candidates'):
        consultant = st.selectbox("Consultant", ["Chris", "Max"])
        client_name = st.text_input("Client Name")
        vacancy = st.text_input("Vacancy")
        candidates = st.text_area("Candidates (Enter each candidate's salary on a new line)")
        currency = st.selectbox("Currency", ["£", "$", "€"])
        fee_percent = st.number_input("Fee %", min_value=0.0, max_value=100.0)
        probability_percent = st.number_input("Probability %", min_value=0.0, max_value=100.0)
        vat = st.selectbox("VAT Applicable?", ["Yes", "No"])
        estimated_month = st.selectbox("Estimated Month of Projection", [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ])
        
        submit_button = st.form_submit_button(label='Add to Pipeline')
        
        if submit_button:
            # Process candidate salaries
            candidate_salaries = [float(salary.strip()) for salary in candidates.split('\n') if salary.strip()]
            if candidate_salaries:
                min_salary = min(candidate_salaries)
                fee_pounds = min_salary * (fee_percent / 100)
                probability_pounds = fee_pounds * (probability_percent / 100)
                
                new_entry = {
                    'Consultant': consultant,
                    'Client Name': client_name,
                    'Vacancy': vacancy,
                    'Candidates': ', '.join(map(str, candidate_salaries)),
                    'Currency': currency,
                    'Fee %': fee_percent,
                    'Fee £': fee_pounds,
                    'Probability %': probability_percent,
                    'Probability £': probability_pounds,
                    'VAT': vat,
                    'Estimated Month': estimated_month
                }
                
                pipeline_data = pipeline_data.append(new_entry, ignore_index=True)
                st.success('Entry added to pipeline!')

def offered_pipeline():
    display_logo()
    st.title("Offered Pipeline")
    
    global offered_data
    
    if not offered_data.empty:
        st.dataframe(offered_data)
        
        for i in range(len(offered_data)):
            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"Move to Invoiced {i}", key=f"inv_{i}"):
                    invoice_data.append(offered_data.iloc[i])
                    offered_data.drop(i, inplace=True)
                    st.success('Moved to Invoiced!')
            with col2:
                if st.button(f"Reject {i}", key=f"rej_{i}"):
                    rejected_data.append(offered_data.iloc[i])
                    offered_data.drop(i, inplace=True)
                    st.warning('Moved to Rejected!')
                    
def invoice_pipeline():
    display_logo()
    st.title("Invoice Pipeline")
    
    global invoice_data
    
    if not invoice_data.empty:
        invoice_data['Start Date'] = pd.to_datetime(invoice_data['Estimated Month'], format='%B')
        invoice_data['Payment Terms'] = 30
        
        invoice_data['Due Date'] = invoice_data['Start Date'] + pd.to_timedelta(invoice_data['Payment Terms'], unit='d')
        
        invoice_data['Paid'] = False
        
        for i in range(len(invoice_data)):
            col1, col2, col3 = st.columns(3)
            with col1:
                if not invoice_data.at[i, 'Paid']:
                    if col1.checkbox(f"Mark as Paid {i}", key=f"paid_{i}"):
                        invoice_data.at[i, 'Paid'] = True
                        st.success('Invoice marked as paid!')
            
            with col2:
                if not invoice_data.at[i, 'Paid']:
                    overdue_days = (pd.Timestamp.now() - invoice_data.at[i, 'Due Date']).days
                    if overdue_days > 0:
                        col2.error(f"Overdue by {overdue_days} days")

def rejected_pipeline():
    display_logo()
    st.title("Rejected Pipeline")
    
    global rejected_data
    
    if not rejected_data.empty:
        st.dataframe(rejected_data)

def stats_page():
    display_logo()
    st.title("Stats Page")
    
    total_candidates = len(pipeline_data) + len(offered_data) + len(invoice_data) + len(rejected_data)
    
    stats = {
        "Total Candidates": total_candidates,
        "Total Fees": pipeline_data['Fee £'].sum(),
        "Average Fee": pipeline_data['Fee £'].mean() if not pipeline_data.empty else 0,
        "Total Probability Value": pipeline_data['Probability £'].sum()
    }
    
    for key, value in stats.items():
        st.write(f"{key}: {value}")
    
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
    with st.sidebar:
        display_logo()
        
        selection = st.radio("Go to", list(pages.keys()))
        
        page_function = pages[selection]
        
        page_function()

if __name__ == "__main__":
    main()
