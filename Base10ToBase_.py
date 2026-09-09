def Base10ToBase_(num, base):
    import string
    if num == 0: return "0"
    if base < 2 or base > 36: return "2 <= base <= 36."

    negative = False
    if num < 0:
        negative = True
        num *= -1

    convertedNum = ""
    chars = string.digits + string.ascii_uppercase
    while num != 0:
        remain = num % base
        convertedNum += chars[remain]
        num //= base

    if negative == True:
        convertedNum += "-"
    return convertedNum[::-1]

if __name__ == "__main__":
    print(Base10ToBase_(123, 2)) #num, base