def divide_by_zero():
    try:
        result = 5 / 0
    except ZeroDivisionError:
        print("division by zero error")
divide_by_zero()
