def unique_in_order(sequence):
    list = []
    for i in range(len(sequence)):
        if i == 0 or sequence[i] != sequence[i-1]:
            list.append(sequence[i])
    return list 