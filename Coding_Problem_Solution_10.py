# asked by Airbnb.
# Given a list of integers, write a function that returns the largest sum of
# non-adjacent numbers. Numbers can be 0 or negative.
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
# [5, 1, 1, 5] should return 10, since we pick 5 and 5.
# Follow-up: Can you do this in O(N) time and constant space?


def max_sum(l):
    if not l:
        return 0
    elif len(l)<=2:
        return max(l)
    
    last_num=l[-1]
    with_last=max_sum(l[:-2])+last_num
    without_last=max_sum(l[:-1])
    return max(with_last, without_last)

def main():
    input_list=[int(i) for i in input("Enter the list: ").split()]
    print("Max sum of non adjacent numbers is {0}".format(max_sum(input_list)))

if __name__=='__main__':
    main()
    
            
