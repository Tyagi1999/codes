# Best Time to Buy and Sell Stock

# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
# Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

'''
Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
'''


def max_profit(inp):
    i=0
    valley=inp[0]
    peak=inp[0]
    maxprofit=0

    while i < len(inp)-1:
        while i < len(inp)-1 and inp[i]>=inp[i+1]:
            i+=1
        valley=inp[i]

        while i < len(inp)-1 and inp[i]<=inp[i+1]:
            i+=1
        peak=inp[i]

        maxprofit+=peak-valley
    return maxprofit

''' Another method to solve this problem '''

def max_profit_2(inp):
    maxprofit=0
    for i in range(1,len(inp)):
        if inp[i]>inp[i-1]:
            maxprofit+=inp[i]-inp[i-1]
    return maxprofit        

inp=[int(x) for x in input("enter the input: ").split()]
print(max_profit(inp))
print(max_profit_2(inp))
