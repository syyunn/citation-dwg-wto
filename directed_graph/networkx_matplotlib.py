# libraries
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Build a dataframe with your connections
# df = pd.DataFrame({'from': ['Tariff Concession ', 'B', 'C', 'A'], 'to': ['Quantitative Restriction', '', 'E', 'C'], 'value': [1, 10, 5, 5]})
df = pd.DataFrame({ 'from':['A', 'B', 'C','A'], 'to':['D', 'A', 'E','C'], 'value':[20, 10, 5, 5]})


# Build your graph
G = nx.from_pandas_edgelist(df, 'from', 'to', create_using=nx.Graph())

# Custom the nodes:
nx.draw(G, with_labels=True, node_color='skyblue', node_size=1500, edge_color=df['value'], width=10.0,
        edge_cmap=plt.cm.Blues)

# plt.show()
import tikzplotlib
tikzplotlib.save('../market_access.tex')
if __name__ == "__main__":
    pass
