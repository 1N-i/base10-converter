from Base10ToBase_ import Base10ToBase_
from Base_ToBase10 import Base_ToBase10

def BaseXToBaseY(num, originalBase, destinedBase):
    num_base10 = Base_ToBase10(num, originalBase)
    return Base10ToBase_(num_base10, destinedBase)

if __name__ == "__main__":
    while True:
        try:
            num = input("Number to convert: ")
            originalBase = int(input("Original base: "))
            destinedBase = int(input("Base to convert: "))

            result = BaseXToBaseY(num, originalBase, destinedBase)
            print(f"Result: {result}")
            break
        except ValueError as e:
            print(f"Error: {e}\nTry again.\n")