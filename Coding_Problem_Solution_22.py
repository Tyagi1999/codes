# asked by Snapchat
# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping),
# find the minimum number of rooms required.
# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

#input_list=[(30,75),(0,50),(60,150)]
input_list=[(90,91), (94, 120), (95, 112), (110, 113), (150, 190), (180, 200)]
start_list=[]
end_list=[]
for i in input_list:
    start_list.append(i[0])

for i in input_list:
    end_list.append(i[1])

start_list.sort()
end_list.sort()

i=j=0
temp_room=room_req=0
n=len(input_list)

while i<n and j<n:
    if start_list[i]<end_list[j]:
        temp_room+=1
        room_req=max(temp_room,room_req)
        i+=1
    else:
        temp_room-=1
        j+=1

print("Rooms required are: {0}".format(room_req))        
