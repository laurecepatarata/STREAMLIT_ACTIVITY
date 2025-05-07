import streamlit as st
import pandas as pd

st.title("📊 Excel DataFrame Viewer")

# Allow Excel file upload
uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx"])

if uploaded_file is not None:
    try:
        # Load Excel file using pandas
        data = pd.read_excel(uploaded_file)

        # Check for minimum column count
        if data.shape[1] < 5:
            st.error("The uploaded file must contain at least 5 columns.")
        else:
            st.success("File uploaded successfully!")

            # Checkbox to toggle raw data display
            if st.checkbox("Show raw data"):
                st.subheader("Raw Data")
                st.dataframe(data)

            # Column selection for filtering
            selected_column = st.selectbox("Select a column to filter by", data.columns)
            unique_values = data[selected_column].dropna().unique()

            selected_value = st.selectbox(
                f"Filter rows where `{selected_column}` is:",
                sorted(unique_values.astype(str))
            )

            # Filter the DataFrame
            filtered_data = data[data[selected_column].astype(str) == selected_value]

            st.subheader(f"Filtered Data (where `{selected_column}` = {selected_value})")
            st.dataframe(filtered_data)

    except Exception as e:
        st.error(f"Error loading file: {e}")
else:
    st.info("Please upload an Excel file to begin.")