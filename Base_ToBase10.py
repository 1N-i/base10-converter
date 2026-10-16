import string
def Base_ToBase10(num, originalBase):
    if not isinstance(num, str):
        num = str(num)
    num = num.strip().upper()

    if num == "0" or not num or num == "-":
        return 0
        
    if originalBase < 2 or originalBase > 36:
        raise ValueError("Base should be between 2 and 36")

    negative = False
    if num[0] == "-":
        negative = True
        num = num[1:]

    chars = string.digits + string.ascii_uppercase
    valid_chars = chars[:originalBase]
    
    for char in num:
        if char not in valid_chars:
            raise ValueError(f"'{char}' is invalid to the base {originalBase}.")

    charMap = {char: i for i, char in enumerate(chars)}
    convertedNum = 0
    
    for exponent, char in enumerate(reversed(num)):
        convertedNum += charMap[char] * (originalBase ** exponent)

    if negative:
        convertedNum *= -1
        
    return convertedNum

if __name__ == "__main__":
    while True:
        try:
            num = input("Number to convert: ")
            originalBase = int(input("Original base: "))

            result = Base_ToBase10(num, originalBase)
            print(f"Result: {result}")
            break
        except ValueError as e:
            print(f"Error: {e}\nTry again.\n")