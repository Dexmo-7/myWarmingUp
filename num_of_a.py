def count_of_a(values:list):
    total = list(map(lambda number: number.count("a"), values))
    return total

print(count_of_a(["aligator", "anka", "dog"]))