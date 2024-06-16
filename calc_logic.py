# библиотека для работы с регулярными выражениями
import re
result = None
_incom_text = input('Введите выражение:')
ALL_SYMBOLS = ['**', '//', '*', '+', '-', '/', '%']
# экранируем специальные символы, добавляем их в строку, разделяя знаком '|' (или)
regex_str = '|'.join(re.escape(symbol) for symbol in ALL_SYMBOLS)
# создаем список из введенных чисел (делим по символам операндов из regex_str)
income_digits = re.split(regex_str, _incom_text)
# создаем список из введенных операндов, добавляя их в заданной последовательности
actual_symbols = re.findall(regex_str, _incom_text)
while len(income_digits) > 1:
    for operation in actual_symbols:
        if operation == '**':
            index = actual_symbols.index(operation)
            actual_symbol = actual_symbols.pop(index)
            operand_1 = income_digits.pop(index)
            operand_2 = income_digits.pop(index)
            result = int(operand_1) ** int(operand_2)
            income_digits.insert(index, result)

    for operation in actual_symbols:
        if operation in '//, *, /, %':
            index = actual_symbols.index(operation)
            actual_symbol = actual_symbols.pop(index)
            operand_1 = income_digits.pop(index)
            operand_2 = income_digits.pop(index)
            match actual_symbol:
                case '//':
                    result = int(operand_1) // int(operand_2)
                case '*':
                    result = int(operand_1) * int(operand_2)
                case '/':
                    result = int(operand_1) / int(operand_2)
                case '%':
                    result = int(operand_1) % int(operand_2)
            income_digits.insert(index, result)

    for operation in actual_symbols:
        if operation in '+, -':
            index = actual_symbols.index(operation)
            actual_symbol = actual_symbols.pop(index)
            operand_1 = income_digits.pop(index)
            operand_2 = income_digits.pop(index)
            match actual_symbol:
                case '+':
                    result = int(operand_1) + int(operand_2)
                case '-':
                    result = int(operand_1) - int(operand_2)
            income_digits.insert(index, result)
print(result)
