import random

def mergSort(arr):
	if len(arr) <= 1: 
		return arr 								#can't sort nothin
	else:
		split = random.randint(1,len(arr)-1)	#randomsly split array 
		left = mergSort(arr[:split])			#recursion on left to sort
		right = mergSort(arr[split:])			#recursion on right to sort
		sortedArr = mergeDem(left,right)		#sort the left and right and combine
		return sortedArr						#return dis bish

def mergeDem(left,right):
	sorted=[]
	lind = rind = 0
	while lind < len(left) and rind < len(right):	#while still got somthin to sort
		if left[lind] < right[rind]:				#left smaller than right
			sorted.append(left[lind])				
			lind += 1
		else:										#right smaller than left
			sorted.append(right[rind])
			rind += 1

	#dis cause there might be left over terms (already sorted) uneven sides bro
	sorted += right[rind:]
	sorted += left[lind:]

	return sorted 				#go home bish

print(mergSort([9,5,2,7,3,6,4,1]))		#example yo