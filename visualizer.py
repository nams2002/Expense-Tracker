import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# File to store expenses
DATA_FILE = "expense_data.csv"

# Plot spending trend
def plot_spending_trend():
    df = pd.read_csv(DATA_FILE)
    df["Date"] = pd.to_datetime(df["Date"])
    daily_spending = df.groupby("Date").sum()
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=daily_spending, x="Date", y="Amount", marker="o")
    plt.title("Daily Spending Trend")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.grid(True)
    return plt.gcf()
