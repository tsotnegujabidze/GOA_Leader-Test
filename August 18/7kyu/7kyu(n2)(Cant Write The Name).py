def is_divisible(number, *arguments):
    ll = arguments
    for something in ll:
        if number % something != 0:
            return False
    return True