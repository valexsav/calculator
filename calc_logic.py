_incom_text = input('Введите выражение:')
result = None
income_digits = []
MATH_SYMBOLS = None
digits = []
symbols = ['//', '*', '+', '-']
for symb in symbols:
    if symb in _incom_text:
        MATH_SYMBOLS = symb
        income_digits = _incom_text.split(MATH_SYMBOLS)
        break
if MATH_SYMBOLS == symbols[0]:
    result = int(income_digits[0]) // int(income_digits[1])
elif MATH_SYMBOLS == symbols[1]:
    result = int(income_digits[0]) * int(income_digits[1])
elif MATH_SYMBOLS == symbols[2]:
    result = int(income_digits[0]) + int(income_digits[1])
elif MATH_SYMBOLS == symbols[3]:
    result = int(income_digits[0]) - int(income_digits[1])
print(f'Ответ:{result}')
