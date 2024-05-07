#TODO
from random import random
import pandas as pd

class ABTesting:
 def __init__(self, groups):
 self.groups = groups
 self.data = {'Group': [], 'Outcome': []}

 def assign_group(self):
 if random() < 0.5:
 return self.groups[0]
 else:
 return self.groups[1]

 def add_data_point(self, group, outcome):
 self.data['Group'].append(group)
 self.data['Outcome'].append(outcome)

 def calculate_conversion_rate(self, group):
 df = pd.DataFrame(self.data)
 return df[df['Group'] == group]['Outcome'].mean()

 def determine_winner(self):
 conversion_rate_a = self.calculate_conversion_rate(self.groups[0])
 conversion_rate_b = self.calculate_conversion_rate(self.groups[1])
 if conversion_rate_a > conversion_rate_b:
 return self.groups[0]
 else:
 return self.groups[1]

ab_testing = ABTesting(['A', 'B'])
for _ in range(10000):
 group = ab_testing.assign_group()
 outcome = int(random() < 0.1) if group == 'A' else int(random() < 0.11)
 ab_testing.add_data_point(group, outcome)
print(ab_testing.determine_winner())
