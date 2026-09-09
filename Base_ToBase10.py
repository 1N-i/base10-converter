def Base_ToBase10(num, originalBase):
    import string
    if num == "0" or not num: return 0
    if originalBase < 2 or originalBase > 36: return "2 <= base <= 36."

    negative = False
    if num[0] == "-":
        negative = True
        num = num[1:]

    chars = string.digits + string.ascii_uppercase
    charMap = {char: i for i, char in enumerate(chars)}
    convertedNum = 0
    
    for exponent, char in enumerate(reversed(num)):
        convertedNum += charMap[char.upper()] * (originalBase ** exponent)

    if negative == True:
        convertedNum *= -1
    return convertedNum

if __name__ == "__main__":
    print(Base_ToBase10("-7B", 16)) #"num", originalBase