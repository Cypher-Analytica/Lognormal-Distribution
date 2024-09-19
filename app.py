# Import necessary libraries
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import lognorm, norm

# Set the title of the Streamlit app
st.title("Lognormal Distribution Visualization with Log Transformation")

# Description of the app
st.write("""
This app visualizes the Lognormal Distribution and its log transformation.
Adjust the parameters below to see how they affect the shape of the distribution.
""")

# Input sliders for parameters of the lognormal distribution
mean = st.slider("Mean of the underlying normal distribution (µ)", min_value=0.0, max_value=3.0, value=0.0, step=0.1)
sigma = st.slider("Standard deviation (σ)", min_value=0.1, max_value=2.0, value=0.5, step=0.1)

# Compute the scale parameter for the lognormal distribution
scale = np.exp(mean)

# Generate x values and the corresponding y values for the lognormal PDF
x = np.linspace(0.01, 5, 1000)
pdf = lognorm.pdf(x, s=sigma, scale=scale)

# Sample data points from the lognormal distribution
sample_data = lognorm.rvs(s=sigma, scale=scale, size=1000)
log_transformed_data = np.log(sample_data)  # Log-transform the sampled data

# Plotting the original Lognormal distribution and its log-transformed version
fig, ax = plt.subplots(1, 2, figsize=(16, 5))

# Plotting the original Lognormal distribution
ax[0].plot(x, pdf, label=f'Lognormal PDF (µ={mean}, σ={sigma})', color='blue')
ax[0].fill_between(x, pdf, alpha=0.2, color='blue')
ax[0].set_title('Lognormal Distribution')
ax[0].set_xlabel('x')
ax[0].set_ylabel('Probability Density')
ax[0].legend()

# Plotting the log-transformed data (should resemble a normal distribution)
sns.histplot(log_transformed_data, kde=True, stat="density", bins=30, color='red', ax=ax[1])
ax[1].set_title('Log-Transformed Data (Normal Distribution)')
ax[1].set_xlabel('Log(x)')
ax[1].set_ylabel('Density')

# Display both plots side by side
st.pyplot(fig)

# Additional information about the distribution
st.write("""
### Understanding the Parameters and Log Transformation:
- **Mean (µ)**: The mean of the underlying normal distribution. Affects the location of the lognormal distribution.
- **Standard Deviation (σ)**: The spread of the underlying normal distribution. Higher values lead to a wider distribution.
- **Log Transformation**: The natural log transformation converts lognormally distributed data back to a normal distribution scale.
""")

