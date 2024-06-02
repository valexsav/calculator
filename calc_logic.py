_incom_text = input('Введите выражение:')
result = ''
income_digits = []
_actually_symbol = 0
digits = []
symbols = ['//', '*', '+', '-']
for i in range(0, 10):
    digits.append(i)
for symb in symbols:
    if symb in _incom_text:
        _actually_symbol = symb
        income_digits = _incom_text.split(_actually_symbol)
if _actually_symbol == symbols[0]:
    result = int(income_digits[0]) // int(income_digits[1])
elif _actually_symbol == symbols[1]:
    result = int(income_digits[0]) * int(income_digits[1])
elif _actually_symbol == symbols[2]:
    result = int(income_digits[0]) + int(income_digits[1])
elif _actually_symbol == symbols[3]:
    result = int(income_digits[0]) - int(income_digits[1])
print(f'Ответ:{result}')
