import random

# set roman numeral values
roman_values = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC",
                50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}


def convert_num(num):
    roman_num = ''
    while num > 0:
        for i in roman_values:
            if num == 0:
                break
            else:
                while num >= i:
                    roman_num += roman_values[i]
                    num -= i
    return roman_num


test_value = random.randint(1, 3000)
print(test_value)
print(convert_num(test_value))