# asked by Facebook
# A builder is looking to build a row of N houses that can be of K different colors.
# He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.
# Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color
# return the minimum cost which achieves this goal.

def solution(costs):
    best=[0]*len(costs[0])
    for cost in costs:
        temp=[0]*len(costs[0])
        for index in range(len(cost)):
            temp[index]=cost[index]+min(best[:index]+best[index+1:])

        best=temp
        print(best)

    return min(best)

costs=[[2,1,1],
       [1,10,3],
       [1,2,100]]
print("lowest cost possible is: {0}".format(solution(costs)))
