#to Check Monotonic Array
arr=[1,2,2,3,4]
#check for non-decreasing
non_decreasing=all(arr[i]<=arr[i+1] for i in  range (len(arr)-1))
#check for non-increasing
non_increasing=all(arr[i]>=arr[i+1] for i in range(len(arr)-1))
if non_decreasing or non_increasing:
    print("it is a monotonic array")
else:
    print("it is not a monotonic array")