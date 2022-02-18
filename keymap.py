import string

letters = string.ascii_uppercase
alpha_key_list = list(letters)

number_key_list = ["N"+str(x) for x in range(10)]

print(number_key_list)
print(alpha_key_list)
