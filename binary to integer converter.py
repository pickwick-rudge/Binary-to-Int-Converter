arr = [1, 8, 18, 2, 1, 0, 3, 1, 5, 0]

def binary_array_to_number(arr):
    output_num = 0
    exponent = 1
    arr = reversed(arr)
       
    for index,value in enumerate(arr):
        if value > 0:
            output_num += exponent * value
            exponent *= 2
        else:
            exponent *= 2

    return output_num


def binary_array_to_number_2(arr):
    output = 0
    
    for digit in arr:
        output = output * 2 + digit
        
    return output

if binary_array_to_number(arr) == binary_array_to_number_2(arr):
    print('True')

#binary_array_to_number_2 is clearly the better, more elegant solution, though both work

