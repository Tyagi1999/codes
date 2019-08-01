# asked by Facebook

# Given a list of number return all the possible subsets of those numbers.
# for example if given numbers are [1, 2] then its subsets are : {null},{1},{2},{1,2}
# total number of subsets can be found as (2)^n where n is number of items given in list.


def all_subsets(input_list):
    subsets=[0]*len(input_list)
    helper(input_list,subsets,0)

def helper(input_list,subsets,i):
    if i==len(input_list):
        print(subsets)

    else:
        subsets[i]=None
        helper(input_list,subsets,i+1)
        subsets[i]=input_list[i]
        helper(input_list,subsets,i+1)

def main():
    input_list=[int(i) for i in input("enter the numbers: ").split()]
    all_subsets(input_list)

if __name__=='__main__':
    main()
    

        
