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
            eggLayingFreq (float): The probability of a hen laying an egg, must be between 0 and 1.
            name (str): The chicken's name. Just a fun thing, not required.
    """
    def __init__(self, gender:str, eggLayingFreq: float, name: Union[str,int]) -> None:
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
        if((eggLayingFreq < 0) | (eggLayingFreq > 1)):
            print("eggLayingFreq must be beteen zero and one")
            raise ValueError
        if((name is not str)|(name is not int)):
            print("Chicken names must be strings or integers") 
            raise TypeError
        # Assign values
        self.gender = gender
        self.eggLayingFreq = eggLayingFreq
        self.name = name
    
    def getEgg(self, dist:str = 'normal') -> bool():
        """
            Returns TRUE if the chicken lays an egg, else FALSE

            Parameters:
                dist (str): the type of probability distribution that governs egg-laying. Available options are:
                    - **normal** for a Gaussian distribution
                    - **uniform** for a uniform distribution

        """

        # Roosters will never lay eggs
        if(self.gender == 'Rooster'):
            return False

        # Next we get a random number and eval to see if they laid an egg
        else:
            if(dist == 'normal'):
                return True if np.random.normal(0.5, 0.16, 1)[0] <= self.eggLayingFreq else False
            if(dist == 'uniform'):
                return True if np.random.uniform(0., 1., 1)[0] <= self.eggLayingFreq else False

    
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
 