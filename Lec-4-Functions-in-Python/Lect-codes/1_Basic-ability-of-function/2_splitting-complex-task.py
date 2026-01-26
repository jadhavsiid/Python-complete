"""
You're creating a monthly report for cafe's sales. Instead of pullling all logic in one place, break it down.

Task:
- Write a function generate_report() that calls:
      - fetch sales()
      - filter_valid_orders()
      - summarize_data()
"""

def fetch_sales():
    print("Sales are fetched")

def filter_valid_orders():
    print("Valid orders are filtered")

def summarize_data():
    print("Data Summarized")

def generate_report():
    fetch_sales()
    filter_valid_orders()
    summarize_data()

generate_report()