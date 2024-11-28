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
    
    # Allow direct editing of the pipeline table
    edited_pipeline_data = st.experimental_data_editor(pipeline_data, num_rows="dynamic")
    
    # Update the global pipeline data with any changes made in the editor
    if not edited_pipeline_data.equals(pipeline_data):
        pipeline_data = edited_pipeline_data.copy()
        st.success('Pipeline updated successfully!')

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
    
    # Sidebar radio buttons for persistent navigation
    selection = st.sidebar.radio("Go to", list(pages.keys()))
    
    page_function = pages[selection]
    
    page_function()

if __name__ == "__main__":
    main()
