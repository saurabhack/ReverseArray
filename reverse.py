def reverse(arr):
	size=len(arr)
	right=0
	left=size-1
	while(right<left):
		temp=arr[right]
		arr[right]=arr[left]
		arr[left]=temp
		right+=1
		left-=1

	for i in range(size):
		print(arr[i])

if __name__=='__main__':
	arr=[1,2,3,4,5]
	reverse(arr)


