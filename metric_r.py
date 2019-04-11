# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 13:10:42 2018

@author: WSi
"""

import networkx as nx
from networkx.exception import NetworkXError

def metric_r_degree(G):
    """Return the metric R with node degree as node importance measure.
	
    This function is specially provided, since calculating node degree is
	quicker	than calculating degree centrality, which is normalzed in NetworkX.

    Parameters
    ----------
    G : Graph
        The graph for which R is to be computed

    Returns
    -------
    R : float
        The robustness metric R of G.

    """

    total = n = G.number_of_nodes()
    for i in range(1, n) :
        node, max_deg = max(G.degree(), key=lambda x: x[1])
        G.remove_node(node)
        c = max(nx.connected_components(G), key=len)
        total += len(c)
    R = total / n / (n+1)
    return R

def metric_r(G, centrality_func=None):
    """Return the metric R with given centrality as node importance measure.

    This function allows the flexible use of different centralities to 
	calculate R.
	
    Parameters
    ----------
    G : Graph
        The graph for which R is to be computed
    centrality_func : function
        The function for calculating a centality (e.g., betweenness_centrality)

    Returns
    -------
    R : float
        The robustness metric R of G.

    """
    total = n = G.number_of_nodes()
    if centrality_func is None:
        centrality_func = nx.degree_centrality
    for i in range(1, n) :
        node, max_cen = max(centrality_func(G).items(), key=lambda x: x[1])
        G.remove_node(node)
        c = max(nx.connected_components(G), key=len)
        total += len(c)
    R = total / n / (n+1)
    return R

def metric_r_LC(G, centrality_func=None):
    """Return the metric R with only those nodes in the largest component (LC)
       considered.

    This function considers the LC strategy in terms of node removal.
    It also allows the flexible use of different centralities to 
	calculate R.
	
    Parameters
    ----------
    G : Graph
        The graph for which R is to be computed
    centrality_func : function
        The function for calculating a centality (e.g., betweenness_centrality)

    Returns
    -------
    R : float
        The robustness metric R of G.

    """
    total = n = G.number_of_nodes()
    if centrality_func is None:
        centrality_func = nx.degree_centrality
    for i in range(1, n) :
        giant = max(nx.connected_component_subgraphs(G), key=len)
        node, max_cen = max(centrality_func(giant).items(), key=lambda x: x[1])
        G.remove_node(node)
        c = max(nx.connected_components(G), key=len)
        total += len(c)
    R = total / n / (n+1)
    return R
    