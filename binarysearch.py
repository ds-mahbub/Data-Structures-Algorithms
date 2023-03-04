def BinarySearch(arr, target): # Define a function name binary_search/BinarySearch
    lb = 0 # set the lower bound to zero as the index starts at 0
    ub = len(arr)-1 # set the upper bound to length -1 
    while lb <= ub: # compare lower bound and upper bound
        mid =(lb + ub)//2 # find the mid // = int division
        if target == arr[mid]: # if target is equal to mid 
            return mid # mid is the index where we will find the target
        elif target > arr[mid]: # look if the target is less than the mid
            lb = mid + 1 # if the target is less than the mid then increase it by mid + 1
        elif target < arr[mid]: # look if the target is greater than the mid
            ub = mid - 1 # if target is greater than the mid then set the upper bound to mid - 1
        else:
            return -1 # if printed the value is not found in the array
        
arr = [2, 3, 4, 5, 6, 7] # given array
target = 4 # target value
result=BinarySearch(arr,target ) # result
print("Object Found at Index:", result) # printing the result
 


