import string
def Base10ToBase_(num, base):
    if base < 2 or base > 36:
        raise ValueError("Base should be between 2 and 36")

    try:
        num = int(num)
    except ValueError:
        raise ValueError("The number is not valid.")

    if num == 0: return "0"

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

    if negative:
        convertedNum += "-"
        
    return convertedNum[::-1]

if __name__ == "__main__":
    while True:
        try:
            num = input("Number to convert: ")
            destinedBase = int(input("Base to convert: "))

            result = Base10ToBase_(num, destinedBase)
            print(f"Result: {result}")
            break
        except ValueError as e:
            print(f"Error: {e}\nTry again.\n")