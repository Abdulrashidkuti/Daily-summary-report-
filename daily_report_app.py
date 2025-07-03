#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install streamlit openpyxl pandas')


# In[3]:


import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.title("📋 Daily Summary Report Sheet")

# Form UI
with st.form("daily_form"):
    date = st.date_input("1. Date", value=datetime.today())
    name = st.text_input("2. Name")
    num_calls = st.number_input("3. Number of Calls", min_value=0, step=1)
    num_whatsapp = st.number_input("4. Number of WhatsApp Messages", min_value=0, step=1)
    num_invoice = st.number_input("5. Number of Invoice Out", min_value=0, step=1)
    num_customers = st.number_input("6. Potential Customers", min_value=0, step=1)
    discussion = st.text_area("7. Discussion Details")

    submitted = st.form_submit_button("Submit")

# File path
file_path = "daily_report.xlsx"

# Save to Excel on submit
if submitted:
    new_data = {
        "Date": [date],
        "Name": [name],
        "Number of Calls": [num_calls],
        "WhatsApp Messages": [num_whatsapp],
        "Invoices Out": [num_invoice],
        "Potential Customers": [num_customers],
        "Discussion Details": [discussion]
    }

    df_new = pd.DataFrame(new_data)

    # Check if file exists and append
    if os.path.exists(file_path):
        df_existing = pd.read_excel(file_path)
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    else:
        df_combined = df_new

    # Save to Excel
    df_combined.to_excel(file_path, index=False)
    st.success("✅ Report submitted and saved to Excel successfully!")


# In[4]:


streamlit run daily_report_app.py


# In[ ]:




