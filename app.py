import streamlit as st
import pandas as pd
import os

# Function to load data based on selected state, district, and taluka
def load_data(state, district, taluka):
    file_path = os.path.join(state, district)
    df = pd.read_excel(file_path, sheet_name=taluka)
    return df

# Main function to run the Streamlit app
def main():
    st.title("Population Data Viewer For Genericart")

    # Get list of states
    states = os.listdir()

    # Dropdown to select state
    selected_state = st.selectbox("Select State", states)

    # Get list of districts in selected state
    districts = os.listdir(selected_state)

    # Dropdown to select district
    selected_district = st.selectbox("Select District", districts)

    # Get list of talukas in selected district
    talukas = pd.ExcelFile(os.path.join(selected_state, selected_district)).sheet_names

    # Dropdown to select taluka
    selected_taluka = st.selectbox("Select Taluka", talukas)

    # Submit button
    if st.button("Submit"):
        # Load data based on selected state, district, and taluka
        df = load_data(selected_state, selected_district, selected_taluka)

        # Show data
        st.write("Population Data:")
        st.write(df)

if __name__ == "__main__":
    main()
