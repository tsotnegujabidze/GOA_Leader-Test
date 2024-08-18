def multiply_all(array):
    def multiply(n):
        result = []
        for i in range(0, len(array)):
            dsdsd = array[i]*n
            result.append(dsdsd)
            
        return result
    return multiply