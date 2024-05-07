#TODO
import numpy as np
from scipy import stats

class ABTesting:
    def __init__(self, control_group, treatment_group):
        self.control_group = control_group
        self.treatment_group = treatment_group

    def calculate_conversion_rate(self, group):
        return np.mean(group)

    def calculate_std_err(self, group):
        return np.std(group) / np.sqrt(len(group))

    def calculate_z_score(self):
        control_conv_rate = self.calculate_conversion_rate(self.control_group)
        treatment_conv_rate = self.calculate_conversion_rate(self.treatment_group)
        control_std_err = self.calculate_std_err(self.control_group)
        treatment_std_err = self.calculate_std_err(self.treatment_group)
        pooled_std_err = np.sqrt(control_std_err ** 2 + treatment_std_err ** 2)
        z_score = (treatment_conv_rate - control_conv_rate) / pooled_std_err
        return z_score

    def calculate_p_value(self, z_score):
        p_value = stats.norm.sf(abs(z_score)) * 2  # Two-tailed test
        return p_value

    def run_test(self, alpha=0.05):
        z_score = self.calculate_z_score()
        p_value = self.calculate_p_value(z_score)
        if p_value < alpha:
            print("Reject null hypothesis. The treatment has a significant effect.")
        else:
            print("Fail to reject null hypothesis. The treatment has no significant effect.")

# Example usage
control_group = [0, 1, 1, 0, 1, 0, 1, 1, 0, 1]
treatment_group = [1, 0, 1, 1, 0, 1, 1, 0, 1, 1]
ab_testing = ABTesting(control_group, treatment_group)
ab_testing.run_test()