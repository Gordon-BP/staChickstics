"""
# My first app
Here's our first attempt at using data to create a table:

Statistics questions we want to answer!
1. Given X chickens, what is the probability of choosing a chicken?
2. Given I hens and J roosters, what is the probability of choosing a hen?
3. If a hen lays an egg every k days, what is the probability of picking an egg-laying hen on
    a given day?
4. If the Chickens follow a religion tht prohibits egg-laying on Tuesdays, what is the probability
    of choosing an egg-laying chicken on a given day
5. Depending on the chicken gender and egg status, they will spend a different amount of time, T, on the nest
    T(x) ~ N(gender U egg status) (proper notation?) Roosters spend less nest time, non-egg hens middle, egg hens most.

"""

import streamlit as st
from typing import Union
import pandas as pd
import classes.chicken as Chicken

st.write("Hello World!")
st.write("Welcome to Chicken Statistics Hell~~~")
hen_num = st.slider("Number of hens", 0, 100, int)
egg_freq = st.number_input("Egg laying frequency", 0, 100, int)
rooster_num = st.slider("Number of roosters", 0, 100, int)

def exists(x_list:list, index:int) -> bool:
    """
    Checks if the index i exists in the list

    Parameters:
        x_list (list[any]): the list to test
        index (int): the index to eval
    """

    try:
        x = x_list[index]
        return True

    except IndexError:
        return False

    finally:
        return False

def init_chickens(hen_num:int, rooster_num:int, eggFreq:Union[int, list[int]], nameList:list[str] = []) -> list:
    chicken_list = []
    for i in range(hen_num):
        chicken_list.append(Chicken(
            "Hen",
            eggFreq[i] if(eggFreq is list and exists(eggFreq, i)) else eggFreq,
            nameList[i] if (nameList is list and exists(nameList, i)) else f"{nameList}_{i}"
         )
        )
    for i in range(rooster_num):
        chicken_list.append(Chicken(
            "Rooster",
            0,
            nameList[i] if (nameList is list and exists(nameList, i)) else f"{nameList}_{i}"
         )
        )
    return chicken_list

df = pd.DataFrame({
  'firstrun  column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df
