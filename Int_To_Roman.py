# set roman numeral values
roman_values = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC",
                50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}


# used to encode ints to roman numerals
def encode_num(num):
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


# Used to decode roman numerals to Ints
def decode_num(num):
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


to_convert = 0
completed = False
while not completed:
    enc_dec = input('encode or decode: (enc:dec:quit)')
    if enc_dec == 'enc':
        to_convert = int(input('number to convert:'))
        print(encode_num(to_convert))
        if input('would you like to convert another? (y:n)') == 'n':
            print('thanks for using Int to Roman')
            completed = True
    elif enc_dec == 'dec':
        to_convert = int(input('Roman Numeral to convert:'))
        print(decode_num(to_convert))
        if input('would you like to convert another? (y:n)') == 'n':
            print('thanks for using Int to Roman')
            completed = True
    elif enc_dec == 'quit':
        print('thanks for using Int to Roman')
        completed = True
    else:
        print('no valid selection detected')
