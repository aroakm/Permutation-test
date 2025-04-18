import numpy as np
import matplotlib.pyplot as plt

def function(sample_size):
    """
    Perform a permutation test to assess whether the observed difference
    in means between two groups is statistically significant.

    """

    # Generate random group labels (either 1 or 2)
    conditions = np.random.randint(1, 3, size=sample_size)

    # Generate normally distributed data (mean = 0, std = 1)
    data = np.random.normal(0, 1, size=sample_size)

    # Calculate the true difference in means between the two groups
    true_diff = np.mean(data[conditions == 1]) - np.mean(data[conditions == 2])

    # Skip if there's no difference
    if true_diff == 0:
        return None

    # Array to hold the differences from shuffled data
    shuffle_diff = np.zeros(1000)

    # Perform 1000 permutations: shuffle the condition labels each time
    for i in range(1000):
        np.random.shuffle(conditions)  # Shuffle group labels
        shuffle_diff[i] = np.mean(data[conditions == 1]) - np.mean(data[conditions == 2])

    # Calculate a one-tailed p-value based on the direction of the true difference
    if true_diff > 0:
        p_val = np.sum(shuffle_diff <= true_diff) / 1000
    else:
        p_val = np.sum(shuffle_diff >= true_diff) / 1000

    # Print and return the result of this run
    print(f"The shuffled p-value is = {p_val}")
    return p_val

# Ask the user to define the sample size for the experiment
sample_size = int(input("What is the proposed sample size? "))

# Create an empty list to store the p-values from each run
p_values = []

# Run the permutation test 1000 times to estimate statistical power
for _ in range(1000):
    p = function(sample_size)
    if p is not None:
        p_values.append(p)

# Convert the list of p-values into a NumPy array
p_values = np.array(p_values)

# Calculate the proportion of p-values that were statistically significant (< 0.05)
proportion = np.mean(p_values < 0.05)
print(f"\nThe proportion of returned p-values that are < 0.05 is {proportion:.3f}")

# Plot a histogram of the p-values across all simulations
plt.hist(p_values, bins=20, edgecolor='black', color='skyblue')
plt.axvline(0.05, color='red', linestyle='--', label='p = 0.05 (significance threshold)')
plt.title('Distribution of p-values from 1000 Permutation Tests')
plt.xlabel('p-value')
plt.ylabel('Frequency')
plt.legend()
plt.tight_layout()
plt.show()
