def dating_range(age):
    if age <= 14:
        minimal = int(age - 0.10 * age)
        maximal = int(age + 0.10 * age)
        return f"{minimal}-{maximal}"
    else:
        minimal = int(age / 2 + 7)
        maximal = int((age - 7) * 2)
        return f"{minimal}-{maximal}"