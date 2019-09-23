'''1
   2*3
   4*5*6
   7*8*9*10
   7*8*9*10
   4*5*6
   2*3
   1
'''   


n=8
if n%2==0:
    count=1
    x=n-2
    for i in range(1,(n//2)+1):
        for j in range(1,i+1):
            print(count,end='')
            if j!=i:
                print("*",end='')
            count+=1
        print("")    
    count=count-((n//2)-1)-1
    for i in range(n//2,0,-1):
        for j in range(1,i+1):
            print(count,end='')
            if j!=i:
                print("*",end='')
            count+=1
        print("")    
        count=count-x-1
        x=x-2
        
        
