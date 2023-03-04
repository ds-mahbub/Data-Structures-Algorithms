# def BinarySearch(arr, target):
# 	lb = 0
# 	ub = len(arr) - 1

# 	while lb <= ub:
# 		mid = (lb + ub)//2

# 		if arr[mid] == target:
# 			return mid
# 		elif target > arr[mid]:
# 			lb = mid + 1

# 		else:
# 			ub = mid -1
# arr = [5, 6, 7, 8, 9, 10, 11]
# target = 10
# print(BinarySearch(arr, target))





def BinarySearch(arr, target):
    lb = 0
    ub = len(arr)-1
    while lb <= ub:
        mid =(lb + ub)//2
        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            lb = mid + 1
        elif target < arr[mid]:
            ub = mid - 1
        else:
            return -1
        
arr = [2, 3, 4, 5, 6, 7]
target = 4
result=BinarySearch(arr,target )
print("Object Found at Index:", result)



