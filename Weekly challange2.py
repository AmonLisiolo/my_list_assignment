=-098   	|   `       `       `   `

#0 .
Accept user input as a string
numbers_str = input(" ")01


# Split the input string into a list of strings
numbers_list = numbers_str.split()

# Convert each string in the list to an integer
numbers = [int(num) for num in numbers_list]

# Compute the sum of the integers in the list
total_sum = sum(numbers)

# Print the sum
print(f"The sum of the integers in the list is: {total_sum}")

4-24