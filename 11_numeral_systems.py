def general_conversion(value_str: str, from_base: int, to_base: int, charList: str="0123456789") -> str:
    if (from_base>10 and from_base > len(charList)) or (to_base>10 and to_base > len(charList)):
        return f"invalid charList"
    
    decNumber=0
    for i, digit in enumerate(value_str[::-1]):
        decNumber+=(from_base**i)*charList.index(digit)
    
    value_str_result=""
    i=1
    while i*to_base<decNumber:
        i*=to_base

    #print(decNumber)

    while i>0:
        #print(f"i{i}n{decNumber}//{decNumber//i}")
        value_str_result+=charList[int(decNumber//i)]
        decNumber-= (decNumber//i)*i
        i//=to_base

    return value_str_result
        
def decimal_to_binary(n: int) -> str:
    return general_conversion(str(n), 10, 2)
def binary_to_decimal(binary_str: str) -> int:
    return general_conversion(binary_str, 2, 10)
def decimal_to_hexadecimal(n: int) -> str:
    return general_conversion(str(n), 10, 16, "0123456789abcdef")
def hexadecimal_to_decimal(hex_str: str) -> int:
    return general_conversion(hex_str, 16, 10, "0123456789abcdef")
def decimal_to_base(n: int, base: int) -> str:
    return general_conversion(str(n), "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
def verify_conversions(n: int) -> bool:
    print(f"{hex(n)} == {"0x"+decimal_to_hexadecimal(n)} and {bin(n)} == {"0b"+decimal_to_binary(n)}")
    return (hex(n) == "0x"+decimal_to_hexadecimal(n) and
            bin(n) == "0b"+decimal_to_binary(n))


if __name__ == "__main__":
    # PRO TESTOVÁNÍ: Odkomentujte postupně po implementaci jednotlivých částí.
    print(decimal_to_binary(255))
    print(binary_to_decimal("11111111"))
    print(decimal_to_hexadecimal(255))
    print(hexadecimal_to_decimal("ff"))
    print(verify_conversions(42))
    pass