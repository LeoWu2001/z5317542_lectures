# Write a pay code calculator to compute weekly pay

hours = input("How many hours have you worked in this week?: ")

# converts the string to an integer
hours = int(hours)

base_rate = 51.45
overload_rate = 88.9

if hours > 35:
    pay = (35 * base_rate) + ((hours - 35) * overload_rate)
else:
    pay = hours * base_rate

print(f'This weekly payment is {pay}')