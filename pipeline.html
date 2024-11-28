import streamlit as st
import pandas as pd
import numpy as np

# Sample data initialization
pipeline_data = pd.DataFrame(columns=[
    'Consultant', 'Client Name', 'Vacancy', 'Candidate', 'Salary/Hourly Rate',
    'Currency', 'Fee %', 'Fee £', 'Probability %', 'Probability £',
    'VAT', 'Estimated Month'
])

offered_data = pd.DataFrame(columns=pipeline_data.columns)
invoice_data = pd.DataFrame(columns=pipeline_data.columns)
rejected_data = pd.DataFrame(columns=pipeline_data.columns)

# Function to display the logo and make it clickable
def display_logo():
    st.markdown(
        """
        <a href="/">
            <img src="logo.png" style="position: absolute; top: 10px; right: 10px;" width="100">
        </a>
        """,
        unsafe_allow_html=True
    )

def home_page():
    display_logo()
    st.title("Home Page")
    
    # Dropdown for selecting year and month
    year = st.selectbox("Select Year", ["2024", "2025", "2026"])
    month = st.selectbox("Select Month", [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ])
    
    # Display projected amounts (dummy data for illustration)
    st.write(f"Projected amount for {month} {year}: £{np.random.randint(1000, 10000)}")

def pipeline_page():
    display_logo()
    st.title("Pipeline")
    
    global pipeline_data
    
    # Display current pipeline as a table
    st.dataframe(pipeline_data)
    
    # Form to add new entries
    with st.form(key='add_pipeline'):
        consultant = st.selectbox("Consultant", ["Chris", "Max"])
        client_name = st.text_input("Client Name")
        vacancy = st.text_input("Vacancy")
        candidate = st.text_input("Candidate")
        salary_hourly_rate = st.number_input("Salary/Hourly Rate", min_value=0.0)
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
            fee_pounds = salary_hourly_rate * (fee_percent / 100)
            probability_pounds = fee_pounds * (probability_percent / 100)
            
            new_entry = {
                'Consultant': consultant,
                'Client Name': client_name,
                'Vacancy': vacancy,
                'Candidate': candidate,
                'Salary/Hourly Rate': salary_hourly_rate,
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
    
    # Display offered candidates
    if not offered_data.empty:
        st.dataframe(offered_data)
        
        # Action buttons for each row
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
    
    # Display invoiced candidates
    if not invoice_data.empty:
        invoice_data['Start Date'] = pd.to_datetime(invoice_data['Estimated Month'], format='%B')
        invoice_data['Payment Terms'] = 30  # Assume 30 days payment terms
        
        invoice_data['Due Date'] = invoice_data['Start Date'] + pd.to_timedelta(invoice_data['Payment Terms'], unit='d')
        
        # Add checkbox for paid invoices
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
    
    # Display rejected candidates
    if not rejected_data.empty:
        st.dataframe(rejected_data)

def stats_page():
    display_logo()
    st.title("Stats Page")
    
    # Example statistics (dummy data for illustration)
    
    total_candidates = len(pipeline_data) + len(offered_data) + len(invoice_data) + len(rejected_data)
    
    stats = {
        "Total Candidates": total_candidates,
        "Total Fees": pipeline_data['Fee £'].sum(),
        "Average Fee": pipeline_data['Fee £'].mean() if not pipeline_data.empty else 0,
        "Total Probability Value": pipeline_data['Probability £'].sum()
    }
    
    for key, value in stats.items():
        st.write(f"{key}: {value}")
    
# Main function to run the app
def main():
    pages = {
        "Home": home_page,
        "Pipeline": pipeline_page,
        "Offered": offered_pipeline,
        "Invoice": invoice_pipeline,
        "Rejected": rejected_pipeline,
        "Stats": stats_page,
    }
    
    st.sidebar.title("Navigation")
    
    # Create a button for each page in the sidebar
    if st.sidebar.button("Home"):
        pages["Home"]()
        
    elif st.sidebar.button("Pipeline"):
        pages["Pipeline"]()
        
    elif st.sidebar.button("Offered"):
        pages["Offered"]()
        
    elif st.sidebar.button("Invoice"):
        pages["Invoice"]()
        
    elif st.sidebar.button("Rejected"):
        pages["Rejected"]()
        
    elif st.sidebar.button("Stats"):
        pages["Stats"]()

if __name__ == "__main__":
    main()
