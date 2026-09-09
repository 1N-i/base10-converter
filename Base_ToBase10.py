def Base_ToBase10(num, originalBase):
    import string
    if num == 0: return "0"
    if originalBase < 2 or originalBase > 36: return "2 <= base <= 36."

    chars = string.digits + string.ascii_uppercase
    convertedNum = 0
    num = num[::-1]
    for i in range(len(num)):
        convertedNum += chars.index(num[i].upper()) * (originalBase ** i)

    return convertedNum

if __name__ == "__main__":
    print(Base_ToBase10("7B", 16)) #"num", originalBase