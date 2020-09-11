def length_match(values:list, number:int):
    total = 0
    for value in values:
        if len(value) == number:
            total += 1
    return total

print(length_match(["dog", "cat", "wc", "mini", ""], 0))