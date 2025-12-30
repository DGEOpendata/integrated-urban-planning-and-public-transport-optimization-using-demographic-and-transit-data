python
import pandas as pd
import matplotlib.pyplot as plt

# Load demographic data
demographic_data = pd.read_csv('abu_dhabi_demographics.csv')
# Load public transport data
transport_data = pd.read_json('abu_dhabi_transport.json')

# Merge datasets on a common key, e.g., district
merged_data = pd.merge(demographic_data, transport_data, on='district')

# Analyze transport demand based on demographics
transport_demand = merged_data.groupby(['age_group', 'employment_status']).agg({'ridership': 'sum'})

# Visualize the results
transport_demand.unstack().plot(kind='bar', stacked=True)
plt.title('Transport Demand by Age Group and Employment Status')
plt.xlabel('Age Group')
plt.ylabel('Ridership')
plt.show()
