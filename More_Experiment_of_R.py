"""
@author: Balume
"""
import networkx as nx
import matplotlib.pyplot as plt
import R_metric

try:
    reload
    
except NameError:
    try:
        from importlib import reload  
    except ImportError:
        from imp import reload 

def display_graph(G):
    nx.draw(G)
    plt.show() 
    
def main():
    try:
       
        graphs=input('Enter the number of graphs : ')
        i=0
        while i in range(int(graphs)):
            ''' reload R_metric'''
            reload(R_metric)
            '''Create graph'''
            #G=nx.gnm_random_graph(100,400)
            #G=nx.random_regular_graph(5,20,seed=None)
            G=nx.barabasi_albert_graph(100,50)
            '''display graphs'''            
            display_graph(G)
            '''call  class that return the mertic R with node degree as the node importance measure''' 
            R_metric.metric_r_degree(G)
            i+=1 
       
    except Exception as e:
        print(str(e))
        pass
main()
