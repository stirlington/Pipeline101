import streamlit as st
import pandas as pd

# Initialize session state for storing data
if 'offered_list' not in st.session_state:
    st.session_state['offered_list'] = []
if 'contract_offered_list' not in st.session_state:
    st.session_state['contract_offered_list'] = []
if 'invoiced_list' not in st.session_state:
    st.session_state['invoiced_list'] = []
if 'rejected_list' not in st.session_state:
    st.session_state['rejected_list'] = []

# Function to format currency
def format_currency(amount):
    return f"£{amount:,.2f}"

# Function to calculate totals
def calculate_totals():
    perm_offers_total = sum([float(offer.get('fee', 0)) for offer in st.session_state['offered_list']])
    contract_offers_total = sum([float(offer.get('fee', 0)) for offer in st.session_state['contract_offered_list']])
    total_invoiced = sum([float(inv.get('amount', 0)) for inv in st.session_state['invoiced_list']])
    paid_total = sum([float(inv.get('paidAmount', 0)) for inv in st.session_state['invoiced_list']])
    
    return perm_offers_total, contract_offers_total, total_invoiced, paid_total

# Navigation
st.sidebar.title("Navigation")
pages = ["Home", "Perm Pipeline", "Contractor Pipeline", "Perm Offers", "Contractor Offers", "Rejected/Failed", "Invoiced", "Stats"]
selection = st.sidebar.radio("Go to", pages)

# Home Page
if selection == "Home":
    st.title("Recruitment Dashboard")
    perm_offers_total, contract_offers_total, total_invoiced, paid_total = calculate_totals()
    
    # Display Quick Stats
    st.subheader("Quick Stats")
    st.metric(label="YTD Invoiced", value=format_currency(total_invoiced))
    st.metric(label="Paid Total", value=format_currency(paid_total))
    st.metric(label="Total Perm Pipeline", value=format_currency(perm_offers_total))
    st.metric(label="Total Contract Pipeline", value=format_currency(contract_offers_total))

# Perm Pipeline Page
elif selection == "Perm Pipeline":
    st.title("Perm Pipeline")
    # Display Perm Pipeline Data (Placeholder)
    perm_pipeline_df = pd.DataFrame(st.session_state['offered_list'])  # Example dataframe
    if not perm_pipeline_df.empty:
        st.table(perm_pipeline_df)

# Contractor Pipeline Page
elif selection == "Contractor Pipeline":
    st.title("Contractor Pipeline")
    # Display Contractor Pipeline Data (Placeholder)
    contractor_pipeline_df = pd.DataFrame(st.session_state['contract_offered_list'])  # Example dataframe
    if not contractor_pipeline_df.empty:
        st.table(contractor_pipeline_df)

# Perm Offers Page
elif selection == "Perm Offers":
    st.title("Perm Offers")
    # Display Perm Offers Data (Placeholder)
    perm_offers_df = pd.DataFrame(st.session_state['offered_list'])  # Example dataframe
    if not perm_offers_df.empty:
        st.table(perm_offers_df)

# Contractor Offers Page
elif selection == "Contractor Offers":
    st.title("Contractor Offers")
    # Display Contractor Offers Data (Placeholder)
    contractor_offers_df = pd.DataFrame(st.session_state['contract_offered_list'])  # Example dataframe
    if not contractor_offers_df.empty:
        st.table(contractor_offers_df)

# Rejected/Failed Page
elif selection == "Rejected/Failed":
    st.title("Rejected/Failed")
    # Display Rejected Candidates Data (Placeholder)
    rejected_df = pd.DataFrame(st.session_state['rejected_list'])  # Example dataframe
    if not rejected_df.empty:
        st.table(rejected_df)

# Invoiced Page
elif selection == "Invoiced":
    st.title("Invoiced")
    # Display Invoiced Data (Placeholder)
    invoiced_df = pd.DataFrame(st.session_state['invoiced_list'])  # Example dataframe
    if not invoiced_df.empty:
        st.table(invoiced_df)

# Stats Page
elif selection == "Stats":
    st.title("Pipeline Statistics")
    
    # Placeholder for stats calculations and visualizations
