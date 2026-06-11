'''
stores.py
This file is intended to house all the creation and simulation of retail stores including price variation between
brands, locations, and individual stores.
Author: Devin Lepur
4/16/26
'''


class retail_store():
  
    def __init__(self, location, brand, individual_markup):
        '''
        Docstring for __init__
        
        :param self: 
        :param location: An ordered pair of coordinates ranging from 0-1 indicating location
        :param brand: A string corresponding to the brand of which the store belongs
        :param individual_markup: An int corresponding to the percent the store markups over base
        '''
        self.location = location
        self.brand = brand
        self.individual_markup = individual_markup



class product():
    def __init__(self, name, wholesale_cost):
        '''
        Docstring for __init__
        
        :param name: A string corresponding to the name of the product
        :param wholesale_cost: float corresponding to the base price of the product
        '''
        self.name = name
        self.wholesale_cost = wholesale_cost

# Store creation
