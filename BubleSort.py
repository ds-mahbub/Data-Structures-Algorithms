def BubleSort(nums): # define a function which will take an array
	n = len(nums) # length of the array
	flag = 1
	print("Before Sort: ", nums) # will print the given array

	for i in range(len(nums)-1): 
		print("Iteration:", i)
		flag = 1

		for j in range(0, n-i-1):
			if nums[j]>nums[j+1]:
				temp = nums[j]
				nums[j] = nums[j+1]
				nums[j+1] = temp
				flag = 0
			print(nums)
		if flag == 1:
			break

nums = [4, 6, 1, 5, 3]

BubleSort(nums)

print("\nAfter Sort:", nums)
