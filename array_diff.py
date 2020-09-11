def array_diff(a, b):
    c = b
    for item in a:
        if item not in b:
            c.append(item)
        else:
            c.remove(item)
    return c

def list_create():
    return list(set(map(int, input().split(" "))))

def main_func():
    try:
        a = list_create() 
        b = list_create()
        return sorted(array_diff(a, b))
    except (ValueError, TypeError):
        print("Caught ValueError or TypeError!")

#------------------------------------------------------------------------------
print("Program takes two lists of numbers and return the list without repeated values")
print("Please enter the values for lists (please use spaces as split marks; split lists ENTER key): ")
print(main_func())
