def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list
input_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(unique_elements(input_list))
