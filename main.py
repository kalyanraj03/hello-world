def stocks(arr):
    min_price=arr[0]
    max_price=0


    for i in range(1,len(arr)):
        if arr[i]<min_price:
            min_price=arr[i]
        else:
            if max_price< arr[i]-min_price:
                max_price=arr[i]-min_price

    return max_price, min_price # return result called max_price

n= int(input("Enter the length of the array"))

arr=[]
for i in range(n):
    arr.append(int(input(f"Enter the {i}th day price of the stock")))

print(stocks(arr))
