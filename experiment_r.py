# -*- coding: utf-8 -*-
"""
Created on Oct 24 13:10:42 2018

@author: WSi
"""

import networkx as nx
import metric_r as rlib

funcs=[nx.betweenness_centrality, nx.closeness_centrality]
#funcs.append(nx.current_flow_betweenness_centrality)
#funcs.append(nx.current_flow_closeness_centrality)

#G = nx.cycle_graph(188)
#G = nx.path_graph(188)
#G = nx.barabasi_albert_graph(100, 3)
#G = nx.gnm_random_graph(100, 294)
G = nx.triangular_lattice_graph(10, 9)
#G = nx.full_rary_tree(3, 294)

graphs = []
num_funcs = len(funcs)
for i in range( num_funcs * 2 ) :
    graphs.append(G.copy())

print("degree R: ", rlib.metric_r_degree(G))

for i in range(num_funcs) :
    func_name = str(funcs[i]).split()[1]
    #print(func_name, funcs[i](graphs[i]))
    r = rlib.metric_r(graphs[i], centrality_func=funcs[i])
    print(func_name, 'R: ', r)

print()
for i in range(num_funcs):
    func_name = str(funcs[i]).split()[1]
    #print(func_name, funcs[i](graphs[i]))
    r = rlib.metric_r_LC(graphs[num_funcs+i], centrality_func=funcs[i])
    print(func_name, 'LC R: ', r)

