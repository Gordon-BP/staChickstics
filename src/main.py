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
import time

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
Imagine the user is a farmer with a population of n chickens. This app should...
    1. Let the user pick a number for n
    2. Let the user explore different distribtutions as different breeds of chickens
"""

# I have no idea how the random umber distribution affects hte number of eggs in a day, week, or momth
# so fuck it, let's find out together!

st.header("First let's explore a uniform distribution")
st.write("Uniform chickens decide how many eggs to lay by spinning a big wheel every morning.")
st.write("The wheel is divided into n slices, each with a number in the range (0, n)")
st.write("Whatever number is ultimately selected, that number of chickens spontaneously lay an egg!")
st.write("Then the chickens go play video games or whatever chickens do.")
generator = default_rng()

fig, ax = plt.subplots()
x_points = range(0,chicken_num)
#ax.plot(x_points, y_points)
ax.hist(x_points, bins=int(np.ceil(chicken_num/10)),density=True)
ax.set_xlabel("Number of Eggs Laid")
ax.set_ylabel("Liklihood")
st.subheader("Predicting the output of a population of Uniform chickens looks like this:")
st.pyplot(fig)

st.write("For a population of n chickens, laying 0, n , or n/2 eggs are all equally likely possibilities.")

st.write("Over the span of a month, the chickens' output looks like this:")
uniform_eggs = generator.integers(0, chicken_num, 7)

fig2, ax2 = plt.subplots()
ax2.plot(
    range(1,8),
    uniform_eggs,
    color='r',
    mouseover=True,
    label='Daily Eggs Laid'
)
ax2.plot(
    range(1,8),
    np.cumsum(uniform_eggs),
    color='b',
    mouseover=True,
    label='Cumulative Eggs'
)
ax2.set_xlabel("Day")
ax2.set_ylabel("Eggs Laid")
for i,j in np.ndenumerate(uniform_eggs):
    ax2.annotate(str(j), xy=(i[0]+1.15, int(np.round(j)-5)), color='r', fontsize=6 )
for i,j in np.ndenumerate(np.cumsum(uniform_eggs)):
    ax2.annotate(str(j), xy=(i[0]+0.9, int(np.round(j)+5)), color='b', fontsize=6 )
ax2.legend()
st.pyplot(fig2)

st.header("but what about Binomial Chickens?")
st.write("Binomial chickens have a more individual approach to egg laying. Every day, each binomial chicken flips their own coin.")
st.write("If the binomial chickens' coin comes up heads, they lay an egg. Otherwise, they don't!")

fig, ax = plt.subplots()
def binom_pdf(x):
    mean = np.mean(x)
    std = np.std(x)
    y_out = 1/(std * np.sqrt(2 * np.pi)) * np.exp( - (x - mean)**2 / (2 * std**2))
    return y_out
x_fill = np.arange(0, chicken_num)
y_fill = binom_pdf(x_fill)
# Plotting the bell-shaped curve
ax.fill_between(x_fill, y_fill, 0)
st.subheader("Predicting the output of a population of Binomial chickens looks like this:")
st.pyplot(fig)

st.write("Look familiar? When there's an equal chance between an event happening or not happening, the binomial curve follows a normal distribution.")
st.write("AKA a bell curve!")

st.write("Over the span of a month, the chickens' output looks like this:")
binomial_eggs = generator.binomial(chicken_num,0.5, 7)
fig3, ax3 = plt.subplots()
ax3.plot(
    range(1,8),
    binomial_eggs,
    color='r',
    label='Daily Eggs Laid'
)
ax3.plot(
    range(1,8),
    np.cumsum(binomial_eggs),
    color='b',
    label='Cumulative Eggs'
)
ax3.set_xlabel("Day")
ax3.set_ylabel("Eggs Laid")
for i,j in np.ndenumerate(binomial_eggs):
    ax3.annotate(str(j), xy=(i[0]+1.15, int(np.round(j)-5)), color='r', fontsize=6 )
for i,j in np.ndenumerate(np.cumsum(binomial_eggs)):
    ax3.annotate(str(j), xy=(i[0]+0.9, int(np.round(j)+5)), color='b', fontsize=6 )
ax3.legend()
st.pyplot(fig3)

st.write("Wow, pretty cool how much more consistent Binomial chickens are compared to Uniform chickens!")
st.subheader("What about Gaussian chickens?")
st.write("Gaussian chickens, like binomial chickens, also flip a coin every day to determin egg status")
st.write("However Gaussian chickens' coins don't have equally weighted outcomes!")
st.write("Use the slider below to set how biased the Gaussian chickens' coins are to land on heads (aka lay an egg)")
bias = st.slider(
    label="Egg liklihood", 
    min_value=0., 
    max_value=1.,
    step=0.1,
    value=0.6)

def normal_pdf(x, bias):
    mean =chicken_num*bias
    std = np.std(x)
    y_out = 1/(std * np.sqrt(2 * np.pi)) * np.exp( - (x - mean)**2 / (2 * std**2))
    return y_out
x_fill = np.arange(0, chicken_num)
y_fill = normal_pdf(x_fill, bias)
fig4, ax4 = plt.subplots()
# Plotting the bell-shaped curve
ax4.fill_between(x_fill, y_fill, 0)
st.subheader("Predicting the output of a population of Binomial chickens looks like this:")
st.pyplot(fig4)

st.write("Over the span of a month, the chickens' output looks like this:")
normal_eggs = np.round(generator.normal(chicken_num*bias,np.std(np.arange(0, chicken_num)), 7))
fig5, ax5 = plt.subplots()
ax5.plot(
    range(1,8),
    normal_eggs,
    color='r',
    label='Daily Eggs Laid'
)
ax5.plot(
    range(1,8),
    np.cumsum(normal_eggs),
    color='b',
    mouseover=True,
    label='Cumulative Eggs'
)
ax5.set_xlabel("Day")
ax5.set_ylabel("Eggs Laid")
for i,j in np.ndenumerate(normal_eggs):
    ax5.annotate(str(int(j)), xy=(i[0]+1.15, int(np.round(j)-5)), color='r', fontsize=6 )
for i,j in np.ndenumerate(np.cumsum(normal_eggs)):
    ax5.annotate(str(int(j)), xy=(i[0]+0.9, int(np.round(j)+5)), color='b', fontsize=6 )
ax5.legend()
st.pyplot(fig5)