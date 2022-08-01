

str1 = '12'
# initializing substring
A = 1
# create a result list
result = []
for i in range(0, len(str1), A):
    # convert to int, after the slicing process
    result.append(int(str1[i : i + A]))

print(result)

first_digit = result[0]
second_digit = result[1]

sum_of_sum = first_digit + second_digit

print(sum_of_sum)