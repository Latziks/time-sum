import math

min1 = 0
second_min = 0
h = 0
second_h = 0

for all_combinations in range(1440):
    sum = min1 + h + second_min + second_h
    min1 += 1
    for every_min_change in range(10):
            if min1 == 10:
                min1 = 0
                second_min += 1
            if second_min == 6:
                min1 = 0
                second_min = 0
                h += 1
    for every_h_change in range(10):
            if h == 10:
                h = 0
                second_h += 1
    
    if sum > 9:
        sum = str(sum)
        A = 1
        result = []
        for digit in range(0, len(sum), A):
            result.append(int(sum[digit : digit + A]))

        first_digit = result[0]
        second_digit = result[1]

        sum = first_digit + second_digit
    
    if sum == 10:
        sum = 1

    with open("all-sums.txt", "a") as file:
        sum = str(sum)
        file.write(sum)
        file.write("\n")
list_of_all_sums = open("all-sums.txt").read().splitlines()
time_count = 0

for all_combinations in range(10):
    time_count = str(time_count)
    the_exact_count = list_of_all_sums.count(time_count)
    time_count = int(time_count)
    print(f"The number: {time_count} appeared {the_exact_count} times")
    time_count += 1

    if the_exact_count == 1:
        smallest_appearing_number = time_count


for i in range(0, len(list_of_all_sums)):
    list_of_all_sums[i] = int(list_of_all_sums[i])

    
print("_________________________________________________________________________________________________\nThe smallest appearing number is: 0\nThe largest appearing number is: 9\nThe least appearing number is 0 (appeared 1 time)\nThe most appearing number is 5 (appeared 162 times)\nThe 2nd most appearing numbers are 4 and 6 (appeared 161 times)\nThe 3rd most appearing numbers are 3 and 7 (appeared 160 times)")