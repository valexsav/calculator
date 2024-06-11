# библиотека для работы с регулярными выражениями
import re
_incom_text = input('Введите выражение:')
ALL_SYMBOLS = ['//', '*', '+', '-', '**', '/', '%']
# экранируем специальные символы, добавляем их в строку, разделяя знаком '|' (или)
regex_str = '|'.join(re.escape(symbol) for symbol in ALL_SYMBOLS)
# создаем список из введенных чисел (делим по символам операндов из regex_str)
income_digits = re.split(regex_str, _incom_text)
# создаем список из введенных операндов, добавляя их в заданной последовательности
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
