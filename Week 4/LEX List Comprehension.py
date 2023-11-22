# Constructs a list from the squares of each element in a list
# only if the value is greater than 150

lst = [2,3,10,14,20,21,25,13,15]
new_lst = [idx ** 2 for idx in lst if idx**2 > 150]
print(f"The new list with values of square greater than 150 is {new_lst}")