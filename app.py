# Import necessary libraries
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import lognorm

# Set the title of the Streamlit app
st.title("Lognormal Distribution Visualization")

# Description of the app
st.write("""
This app visualizes the Lognormal Distribution. 
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

# Plotting the lognormal distribution
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, pdf, label=f'Lognormal PDF (µ={mean}, σ={sigma})', color='blue')
ax.fill_between(x, pdf, alpha=0.2, color='blue')
ax.set_title('Lognormal Distribution')
ax.set_xlabel('x')
ax.set_ylabel('Probability Density')
ax.legend()

# Display the plot in the Streamlit app
st.pyplot(fig)

# Additional information about the distribution
st.write("""
### Understanding the Parameters:
- **Mean (µ)**: The mean of the underlying normal distribution. Affects the location of the lognormal distribution.
- **Standard Deviation (σ)**: The spread of the underlying normal distribution. Higher values lead to a wider distribution.
""")
