def in_list(values:list, element:str):
    for index, value in enumerate(values):
        if value == element:
            return index
    return -1

print("Program show the index in the string of characters.")

values = map(str, input("Please input words/letters separated by comma: ").split(","))
element = input("Which element's index you need to know?: ")

print(in_list(values, element))
