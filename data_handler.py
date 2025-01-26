import pandas as pd

# File to store expenses
DATA_FILE = "expense_data.csv"

# Ensure the CSV exists
def initialize_data_file():
    try:
        pd.read_csv(DATA_FILE)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Date", "Amount", "Category"])
        df.to_csv(DATA_FILE, index=False)

# Add expense to CSV
def add_expense(date, amount, category):
    initialize_data_file()
    df = pd.read_csv(DATA_FILE)
    new_entry = {"Date": date, "Amount": amount, "Category": category}
    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)

    df.to_csv(DATA_FILE, index=False)

# Get summary data
def get_summary(view_type):
    initialize_data_file()
    df = pd.read_csv(DATA_FILE)
    df["Date"] = pd.to_datetime(df["Date"])
    if view_type == "Weekly":
        summary = df.groupby(df["Date"].dt.isocalendar().week).sum(numeric_only=True)

    else:
        summary = df.groupby(df["Date"].dt.month).sum(numeric_only=True)

    return summary
