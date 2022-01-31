def insertoinSort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key


arr=[45,6,13,16,53]
insertoinSort(arr)
for i in range(len(arr)):
    print(arr[i])
