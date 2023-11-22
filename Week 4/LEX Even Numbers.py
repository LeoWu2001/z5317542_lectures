# Write a python function to print the even numbers from a given list

number_list = [0,1,2,3,4,5,6,7,8,9,10,20,22,23,25,29,30,31]
def print_even(numbers):

    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)

    return even_numbers

final_list = print_even(number_list)
print(final_list)