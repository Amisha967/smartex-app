import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import streamlit as st
import pandas as pd
from parser import parse_sms
from classify import classify_sms

st.set_page_config(page_title="Expense Categorizer", layout="centered")
st.title("💸 SMS Expense Categorizer")

uploaded_file = st.file_uploader("📤 Upload a CSV file with 'message' column", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Sample Input Data", df.head())

    result_data = []
    for msg in df['text']:
        parsed = parse_sms(msg)
        parsed["message"] = msg
        parsed["category"] = classify_sms(msg)
        result_data.append(parsed)

    result_df = pd.DataFrame(result_data)
    st.success("✅ Categorization complete")
    st.dataframe(result_df)

    st.bar_chart(result_df['category'].value_counts())