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
    edited_pipeline_data = pipeline_data.copy()

    # Display current pipeline as a table without scrollbars
    edited_pipeline_data['Consultant'] = edited_pipeline_data['Consultant'].apply(
        lambda x: st.selectbox('Consultant', ['Chris', 'Max'], index=['Chris', 'Max'].index(x) if x in ['Chris', 'Max'] else 0)
    )
    
    # Calculate Fee £ and Probability £ automatically based on Salary/Hourly Rate and Fee %
    if not edited_pipeline_data.empty:
        edited_pipeline_data['Fee £'] = edited_pipeline_data['Salary/Hourly Rate'] * (edited_pipeline_data['Fee %'] / 100)
        edited_pipeline_data['Probability £'] = edited_pipeline_data['Fee £'] * (edited_pipeline_data['Probability %'] / 100)
    
    # Display the editable DataFrame
    st.experimental_data_editor(edited_pipeline_data, use_container_width=True)

    # Update global data if changes are made
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
