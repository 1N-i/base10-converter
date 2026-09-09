from Base10ToBase_ import Base10ToBase_
from Base_ToBase10 import Base_ToBase10
def BaseXToBaseY(num, originalBase, destinedBase):
    num = Base_ToBase10(num, originalBase)
    num = Base10ToBase_(num, destinedBase)
    return num

if __name__ == "__main__":
    print(BaseXToBaseY("-1111011", 2, 16)) #"num", originalBase, destinedBase