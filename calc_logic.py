import re
_incom_text = input('Введите выражение:')
all_symbols = ['//', '*', '+', '-', '**', '/', '%']
regex_str = '|'.join(re.escape(symbol) for symbol in all_symbols)
income_digits = re.split(regex_str, _incom_text)
actual_symbols = re.findall(regex_str, _incom_text)
result = int(income_digits.pop(0))
while actual_symbols:
    actual_symbol = actual_symbols.pop(0)
    actual_operand = int(income_digits.pop(0))
    match actual_symbol:
        case '//':
            result //= actual_operand
        case '*':
            result *= actual_operand
        case '+':
            result += actual_operand
        case '-':
            result -= actual_operand
        case '**':
            result **= actual_operand
        case '/':
            result /= actual_operand
        case '%':
            result %= actual_operand
print(result)
