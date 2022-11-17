"""
The purpose of this app is to explore different probability distributions, their shape, and their applicatons.
The big questions we want to answer are:
1. How does following different distributions affect the amount of eggs laid...
    ...over the course of one day
    ...over the course of one week
    ...over the course of one month
2. How do the different variables affect egg laying? Things like:
    * Mean
    * Std Deviation
    * Rate
3. Distributions to explore:
    * Normal
    * Uniform
    * Poisson
    * Pareto
    * Binomial (some eggs vs no eggs)
"""

import streamlit as st
from typing import Union
import pandas as pd
import classes.chicken as Chicken
import numpy as np
from numpy.random import default_rng
import matplotlib.pyplot as plt

st.write("Hello World!")
st.write("Welcome to Chicken Statistics Hell~~~")
chicken_num = st.slider(
    label="Number of chickens", 
    min_value=0, 
    max_value=100,
    value=100,
    step= 1
    )
threshold = st.slider(
    label="Threshold", 
    min_value= 0., 
    max_value= 1., 
    step= 0.1)
dist = st.selectbox("Distribution", ['Uniform', 'Normal', 'Poisson', 'Pareto', 'Binomial'])


"""
Stuff the app should do:
    1. User chooses the number of chickens
    2. User chooses the liklihood a for a chicken to lay an egg in a day
    3. The app calculates the number of eggs expected in a given day, week and month along with confidence intervals
    4. There's an option to run an experiment and calculate the number of eggs by day, week, and month
"""

# I have no idea how the random umber distribution affects hte number of eggs in a day, week, or momth
# so fuck it, let's find out together!

st.header("First let's explore a uniform distribution")
st.write("A discrete uniform distribution looks like this:")
generator = default_rng()

fig, ax = plt.subplots()
x_points = range(0,chicken_num)
#ax.plot(x_points, y_points)
ax.hist(x_points, bins=int(np.ceil(chicken_num/10)),density=True)
ax.set_xlabel("Number of Eggs laid")
ax.set_ylabel("Probability")
st.pyplot(fig)

st.write("So, for a given day, the liklihood distribution for the number of eggs laid looks like:")
uniform_eggs = generator.uniform(0, chicken_num, chicken_num)
fig, ax = plt.subplots()
count, bins, ignored = ax.hist(uniform_eggs, 15, density=True)
#ax.plot(bins, (np.ones_like(bins)+(chicken_num/15)), linewidth=2, color='black')
#ax.text(chicken_num/2, np.ones_like(bins), f"Ideal: {np.round(chicken_num/15, 2)}", color='black')
ax.set_xlabel("Egg quantity")
ax.set_ylabel("Liklohood")
st.pyplot(fig)