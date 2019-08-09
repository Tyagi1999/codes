# asked by Jane Street

# Suppose you are given a table of currency exchange rates, represented as a 2D array.
# Determine whether there is a possible arbitrage: that is, whether there is some sequence of trades you can make,
# starting with some amount A of any currency, so that you can end up with some amount greater than A of that currency.

# There are no transaction costs and you can trade fractional quantities.

'''
Note:
https://www.dailycodingproblem.com/blog/how-to-find-arbitrage-opportunities-in-python/
'''

from math import log
def arbitrage(table):
    transformed_graph=[[-log(edge) for edge in row] for row in table]
    source=0
    n=len(transformed_graph)
    min_dist=[float('inf')]*n
    min_dist[source]=0

    for i in range(n-1):
        for v in range(n):
            for w in range(n):
                if min_dist[w]>min_dist[v]+transformed_graph[v][w]:
                    min_dist[w]=min_dist[v]+transformed_graph[v][w]

    for v in range(n):
        for w in range(n):
            if min_dist[w]>min_dist[v]+transformed_graph[v][w]:
                return True

    return False

table=[[5,12,88],
       [17,17,9],
       [30,94,28]]

print(arbitrage(table))
