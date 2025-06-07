import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset
df = pd.read_csv(r"C:\Users\Owner\OneDrive\Personal\Portfolio\retail_staffing_efficiency_june2024_large.csv")

# Add new metrics
df['Revenue_per_Staff'] = df['Total_Sales'] / df['Staff_On_Shift']
df['Conversion_Rate'] = df['Transactions'] / df['Foot_Traffic']

# Group by store and calculate summary metrics
store_summary = df.groupby('Store_ID').agg({
    'Total_Sales': 'sum',
    'Staff_On_Shift': 'mean',
    'Revenue_per_Staff': 'mean',
    'Conversion_Rate': 'mean'
}).reset_index()

# Export store summary
store_summary.to_csv(r"C:\Users\Owner\OneDrive\Personal\Portfolio\store_efficiency_summary.csv", index=False)
print("Store summary saved as 'store_efficiency_summary.csv'")

# Sort and select top 10 stores by Revenue per Staff
top_stores = store_summary.sort_values(by='Revenue_per_Staff', ascending=False).head(10)

# Create bar chart
plt.figure(figsize=(10, 6))
plt.bar(top_stores['Store_ID'].astype(str), top_stores['Revenue_per_Staff'], color='lightgreen')
plt.title('Top 10 Stores by Avg Revenue per Staff')
plt.xlabel('Store ID')
plt.ylabel('Revenue per Staff ($)')
plt.ylim(160, 175)
plt.xticks(rotation=45)
plt.tight_layout()

# Save and show the chart
plt.savefig(r"C:\Users\Owner\OneDrive\Personal\Portfolio\top_10_revenue_per_staff.png", dpi=300)
plt.show()
