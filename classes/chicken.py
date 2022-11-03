"""
    Defines the different classes for my chicken statistics project!
"""

from typing import Union
import pandas
import numpy as np

class Chicken:
    """
        The base class describing a chicken
        
        Variables:
            gender (str): Either 'Hen' or 'Rooster'
            eggLayingFreq (int): How many days it takes the chicken to lay an egg. For example, 2 means an egg every other day; 1 means an egg every day.
            name (str): The chicken's name. Just a fun thing
            sabbath (int): Chickens are religious and have one day per week they don't work. Should be an int between 1 and 7 corresponding to days of the week.
    """
    def __init__(self, gender:str, eggLayingFreq: int, name: Union[str,int], sabbath:int) -> None:
        # Unit tests
        if(gender is not str):
            print("Chicken gender must be either 'Hen' or 'Rooster")
            raise TypeError
        if((gender != 'Hen') | (gender != 'Rooster')):
            print("Chicken gender must be either 'Hen' or 'Rooster")
            raise ValueError
        if((gender == 'Rooster') & (eggLayingFreq > 0)):
            print('Roosters cannot lay eggs; eggLayingFreq must be zero for Roosters')
            raise ValueError
        if(eggLayingFreq is not int):
            print("eggLayingFreq must be an integer")
            raise TypeError
        if(eggLayingFreq < 0):
            print("eggLayingFreq must be greater or equal to zero")
            raise ValueError
        if((name is not str)|(name is not int)):
            print("Chicken names must be strings or integers") 
            raise TypeError
        if(sabbath not in range(1,7)):
            print("Sabbath day must be an int between 1 and 7")
            raise ValueError
        # Assign values
        self.gender = gender
        self.eggLayingFreq = eggLayingFreq
        self.name = name
        self.sabbath = sabbath
        self.lastEggDay = 0
    
    def getEggsLaid(self, days: list[int]) -> list[int]:
        """
            Returns the number of eggs laid on a given day. Days should be indexed starting at 1

            Parameters:
                self (Chicken): the chicken that is laying eggs
                day (int): what day it is
        """
        egg_list = []

        # First make sure that the right data is passed.
        if(len(days) <= 0):
            print("A list of days must be specified")
            raise ValueError

        # Roosters will never lay eggs, so if the Chicken is a rooster we can save
        # processing time and just pass a list of zeros.
        if(self.gender == 'Rooster'):
            egg_list.append(np.zeros(days, dtype=int))
            return egg_list

        # Next we calculate if the day is an egg-laying day, and, if so
        else:
            for i in range(1,days):
                if days[i]%7 == self.sabbathDay:
                    egg_list.append(0)
                else:
                    if days[i]-self.lastEggDay >= self.eggLayingFreq:
                        egg_list.append(1) 
                    else: 
                        egg_list.append(0)
    
    def cluck_cluck(self, days:int) -> pandas.DataFrame:
        """
        Simulates days number of days as a chicken.

        Parameters:
            self (Chicken): the chicken living its best life
            days (int): how many days the chicken will simulate
        
        Returns:
            data (pandas.DataFrame): a Dataframe with the chicken's life data for the days. 
        """
        df = pandas.DataFrame(
            data = {
                "Nest_Time":getNestTime(self, days),
                "Eggs_Laid":getEggsLaid(self, days),
                "Egg_Weight":getEggWeights(self, days)
            },
            index = range(1, days),
            columns=['Nest_Time', 'Eggs_Laid', 'Egg_Weight']
            )
 