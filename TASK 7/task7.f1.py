import math
C = 50
H = 30
def calculate_value(D):
    return round(math.sqrt((2 * C * D) / H))
input_sequence = input("Enter a comma-separated sequence of values for D: ")
values = [int(x) for x in input_sequence.split(",")]
for value in values:
    Q = calculate_value(value)
    print(f"For D = {value}, Q = {Q}")
