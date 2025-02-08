import streamlit as st
import pandas as pd
from classify import classify

st.title("Log Classification App")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)

        if "source" not in df.columns or "log_message" not in df.columns:
            st.error("CSV must contain 'source' and 'log_message' columns.")
        else:
            if st.button("Predict"):
                # Perform classification
                df["target_label"] = classify(list(zip(df["source"], df["log_message"])))

                # Display results
                st.write("Classified Data:")
                st.dataframe(df)

                # Save classified data to a CSV file
                output_file = "classified_logs.csv"
                df.to_csv(output_file, index=False)

                # Provide download button **only after prediction**
                st.download_button("Download Classified CSV",
                                   data=open(output_file, "rb").read(),
                                   file_name="classified_logs.csv",
                                   mime="text/csv")

    except Exception as e:
        st.error(f"Error: {str(e)}")
