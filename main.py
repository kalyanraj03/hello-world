def stocks(arr):
    min_price=arr[0]
    max_price=0

    for i in range(1,len(arr)):
        if arr[i]<min_price:
            min_price=arr[i]
        else:
            if max_price< arr[i]-min_price:
                max_price=arr[i]-min_price

    return max_price

arr=[4,3,2,1,11]

print(stocks(arr))