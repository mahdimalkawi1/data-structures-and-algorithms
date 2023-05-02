def reverseArray(arr):
    reversed_arr = []
    
    for i in range(len(arr)-1, -1, -1):
        reversed_arr.append(arr[i])
        
    return reversed_arr

input_str = input("Enter values: ")

input_arr = input_str.split(",")

output_arr = reverseArray(input_arr)

for element in output_arr:
    print(element)
