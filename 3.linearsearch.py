def linear_search(array_1, key): # Define a function which will take two parameters array & target
	
	for i in range(len(array_1)): # i = 0 to n-1
		
		if array_1[i] == key: # Check if the value of i is equal to target.
			return i # if yes then return i, which is basically the index.
			break # if found then we need to break the loop.
		
	return -1 # if the target is not present in the array the function will return -1

array_1 = [2, 3, 4, 5, 6, 7]
result = linear_search(array_1, 6)
print(f'Object Found at index: {result}')

result = linear_search(array_1, 14)
print(f'Object Found at index: {result}')
