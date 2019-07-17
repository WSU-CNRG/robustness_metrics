# -*- coding: utf-8 -*-
"""
@author: 30033237
"""
import numpy as np
import networkx as nx
import math

def generate_degree_sequences(n, sum, scale):  
    """
        Parameters
        ----------
        n: total number of nodes, should be an even number
        sum : total number of degrees, should be a multiple of n
        scale: total number of sequences to generate
            
    """

    # Average node degree
    mean = round(sum/n)
    # All nodes have the same degree initially
    array = [mean] * n
    # Partition nodes into left side and right side;
    # Each side has half_n nodes
    half_n = round(n/2)
    # Available degrees to move from left to right
    avail = sum/2 - half_n
    # Number of degrees to move in generating each sequence
    moves = math.floor(avail / scale)
    
    vars=[]
    v=np.var(array)
    vars.append(v)
    for i in range(scale-1):
        for j in range(moves):
            index = np.random.randint(0, half_n)
            # check if it is already degree 1
            while array[index] == 1:
                index = np.random.randint(0, half_n)
            array[index] -= 1

            index = np.random.randint(0, half_n)
            # check if it is already max degree
            while array[index+half_n] == n-1:
                index = np.random.randint(0, half_n)
            array[index+half_n] += 1
        
        # Make sure the sequence is graphical
        while not nx.is_graphical(array):
            k = np.random.randint(0, half_n)
            array[k+half_n] -= 1

            k = np.random.randint(0, half_n)
            # check if it is already max degree
            while array[k+half_n] == n-1:
                k = np.random.randint(0, half_n)
            array[k+half_n] += 1
            
        v=np.var(array)
        vars.append(v)

    return vars

vars=generate_degree_sequences(100,2000,100)
#vars=generate_variance_sequences(30,120,15)
vars.sort()
print(vars)
