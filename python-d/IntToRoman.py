import os

def int_to_roman(num):
    
    val_map = [
        (1000, 'M'),
        (900,  'CM'),
        (500,  'D'),
        (400,  'CD'),
        (100,  'C'),
        (90,   'XC'),
        (50,   'L'),
        (40,   'XL'),
        (10,   'X'),
        (9,    'IX'),
        (5,    'V'),
        (4,    'IV'),
        (1,    'I')
    ]

    result = []
    for val, sym in val_map:
        while num >= val:
            result.append(sym)
            num -= val
    return ''.join(result)

def write_valid_cases(filename="tests/validcases.txt"):
    os.makedirs("tests", exist_ok=True)
    with open(filename, "w") as f:
        for i in range(1, 4000):
            roman = int_to_roman(i)
            f.write(f"{roman}\n")

if __name__ == "__main__":
    write_valid_cases()
    print("tests/validcases.txt dosyası oluşturuldu.")
