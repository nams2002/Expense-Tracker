import pandas as pd
from utils.data_handler import add_expense, get_summary
from utils.visualizer import plot_spending_trend
import streamlit as st

# Initialize Streamlit app
st.title("Personal Expense Tracker")

# Add Expense Section
st.header("Add a New Expense")
date = st.date_input("Date")
amount = st.number_input("Amount", min_value=0.0, step=0.1)
category = st.selectbox("Category", ["Food", "Transport", "Entertainment", "Utilities", "Other"])
if st.button("Add Expense"):
    add_expense(date, amount, category)
    st.success("Expense added successfully!")

# Show Summary Section
st.header("Summary")
view_type = st.radio("View Summary", ["Weekly", "Monthly"])
if st.button("Generate Summary"):
    summary = get_summary(view_type)
    st.write(summary)

# Visualization Section
st.header("Spending Trends")
if st.button("Show Graph"):
    fig = plot_spending_trend()
    st.pyplot(fig)
