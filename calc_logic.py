_incom_text = input('Введите выражение:')
result = None
income_digits = []
MATH_SYMBOL = None
digits = []
symbols = ['//', '*', '+', '-']
for symb in symbols:
    if symb in _incom_text:
        MATH_SYMBOL = symb
        income_digits = _incom_text.split(MATH_SYMBOL)
        break
match MATH_SYMBOL:
    case '//':
        print(int(income_digits[0]) // int(income_digits[1]))
    case '*':
        print(int(income_digits[0]) * int(income_digits[1]))
    case '+':
        print(int(income_digits[0]) + int(income_digits[1]))
    case '-':
        print(int(income_digits[0]) - int(income_digits[1]))
