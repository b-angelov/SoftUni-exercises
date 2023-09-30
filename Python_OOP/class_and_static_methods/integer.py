from re import match

class Integer:

    rom_trans = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

    def __init__(self, value: int):
        self.value = value

    @staticmethod
    def from_float(float_value: float):
        if type(float_value) != float:
            return "value is not a float"
        return Integer(int(float_value))

    @staticmethod
    def from_roman(value: str):
        if not match(r"^M*(CM)?D{0,3}(CD)?C{0,3}(XC)?L{0,3}(XL)?X{0,3}(IX)?V?(IV)?I{0,3}$",value):
            return "Invalid roman numeral."
        trans = Integer.rom_trans
        res = sum(trans[v] if i+1 not in range(len(value)) or trans[v] >= trans[value[i+1]] else -trans[v]  for i,v in enumerate(value))
        return Integer(res)

    @staticmethod
    def from_string(value: str):
        if type(value) != str or not value.isdigit():
            return "wrong type"
        return Integer(int(value))

first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("MCMDX")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
