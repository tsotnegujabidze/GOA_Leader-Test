def smaller(arr):
    result = []
    for numbers in range(len(arr)):
        quantity = 0
        for something in range(numbers + 1, len(arr)):
            if arr[something] < arr[numbers]:
                quantity += 1
        result.append(quantity)
    return result