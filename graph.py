import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def get_nodes(g): 
    return g.number_of_nodes()

def get_edges(g): 
    return g.number_of_edges()

def get_degree(g):
    sum_of_degrees = 0
    for degree in g.degree():
        sum_of_degrees += degree[1]
    return (sum_of_degrees/(get_nodes(g)))

def get_density(g):
    density = 0
    nodes = get_nodes(g)
    edges = get_edges(g)
    if nodes == 1:
        density = 0
    else:
        density = (2*edges)/(nodes*(nodes - 1))
    return density


def get_diameter(g):
    return nx.diameter(g)


def plot_graph(g):
    edge_labels = dict([((n1, n2), d['weight'])
                        for n1, n2, d in g.edges(data=True)])

    pos = nx.spring_layout(g, k=0.3*1/np.sqrt(len(g.nodes())), iterations=900)  # Helps to plot a less clustered graph
    plt.figure("Graph",figsize=(30, 30))                                        
    nx.draw(g, pos=pos, node_size=1000, 
            node_color='lightblue', linewidths=0.25, font_size=9,               # Plotting the graph in spring layout
            font_weight='bold', with_labels=True)
    nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels,               # Adding weighted edges
                                font_color='black', font_size=7, font_weight='bold')

    plt.show()


if __name__ == "__main__":
    G = nx.MultiGraph()                                                         # Initialize a multigraph G

    with open("aves-sparrow-social.edges", "r") as f:                           # Read nodes, edges and weight from input file
            lines = f.readlines()
            for line in lines:
                a, b, c = [c.strip() for c in line.split()][:3]
                G.add_edge(a, b, weight=float(c))
    
    print(f"No. of nodes in Graph: {get_nodes(G)}")
    print(f"No. of edges in Graph: {get_edges(G)}")
    print(f"Average degree of Graph: {get_degree(G)}")
    print(f"Density of Graph: {get_density(G)}")
    print(f"Length of the shortest path between the most distanced nodes: {get_diameter(G)} edges")
    plot_graph(G)




    
