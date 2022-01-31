def bubbleSort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-1-i):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp


arr=[23,45,67,2,46]
bubbleSort(arr)

print("Sorted array : \n")
for i in range(len(arr)):
    print(arr[i])
