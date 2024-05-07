#TODO
import random

class AbTesting:
 def __init__(self, experiment_name, variations):
 self.experiment_name = experiment_name
 self.variations = variations
 self.users = {}

 def add_user(self, user_id):
 if user_id not in self.users:
 variation = random.choice(self.variations)
 self.users[user_id] = variation

 def get_variation(self, user_id):
 return self.users.get(user_id)

 def track metric(self, user_id, metric_name, metric_value):
 print(f"Tracking metric {metric_name}={metric_value} for user {user_id} in experiment {self.experiment_name}")

# Example usage
ab_testing = AbTesting("My Experiment", ["A", "B"])
ab_testing.add_user("user1")
print(ab_testing.get_variation("user1"))
ab_testing.track_metric("user1", "clicks", 10)
