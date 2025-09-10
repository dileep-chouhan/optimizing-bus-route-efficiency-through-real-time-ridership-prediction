import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# --- 1. Synthetic Data Generation ---
# Set a random seed for reproducibility
np.random.seed(42)
# Generate synthetic data for bus ridership
num_days = 365
data = {
    'Date': pd.to_datetime(pd.date_range(start='2023-01-01', periods=num_days)),
    'Time': np.random.choice(['Morning', 'Afternoon', 'Evening'], size=num_days),
    'Route': np.random.choice(['A', 'B', 'C'], size=num_days),
    'Ridership': np.random.randint(10, 200, size=num_days) + np.random.normal(0, 20, size=num_days).astype(int) # Add some noise
}
df = pd.DataFrame(data)
#Introduce seasonality (example)
df['Month'] = df['Date'].dt.month
df['Ridership'] = df['Ridership'] + (df['Month'] * 10) - 60 #Simulate higher ridership in summer months
# --- 2. Data Cleaning and Analysis ---
#Handle negative ridership values (if any)
df['Ridership'] = df['Ridership'].apply(lambda x: 0 if x < 0 else x)
#Calculate average ridership per route and time of day
average_ridership = df.groupby(['Route', 'Time'])['Ridership'].mean().unstack()
# --- 3. Visualization ---
#Plot average ridership by route and time of day
plt.figure(figsize=(10, 6))
average_ridership.plot(kind='bar', stacked=True)
plt.title('Average Bus Ridership by Route and Time of Day')
plt.xlabel('Route')
plt.ylabel('Average Ridership')
plt.legend(title='Time of Day')
plt.grid(True)
plt.tight_layout()
# Save the plot to a file
output_filename = 'ridership_by_route_time.png'
plt.savefig(output_filename)
print(f"Plot saved to {output_filename}")
#Plot daily ridership trend
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Ridership'])
plt.title('Daily Bus Ridership Trend')
plt.xlabel('Date')
plt.ylabel('Ridership')
plt.grid(True)
plt.tight_layout()
#Save the plot to a file
output_filename2 = 'daily_ridership_trend.png'
plt.savefig(output_filename2)
print(f"Plot saved to {output_filename2}")
#Further analysis could involve time series forecasting to predict future ridership.  This example focuses on descriptive statistics and visualization.