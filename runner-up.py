def runner_up():
    try:
        arr = map(int, input().split(" "))
        print(sorted(list(set(arr)))[-2])
    except (TypeError, ValueError):
        print("Caught TypeError or ValueError!")
    finally:
        print("Function was executed...")

print("Program show the second highest entered value.")
print("Please provide the numbers (please use spaces as split marks):")

runner_up()
