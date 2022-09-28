from time import sleep


def CheckLeft(i, expression):
    curent_left = i - 1
    left = ''
    while curent_left != -1:
        if expression[curent_left] != '*' and expression[curent_left] != '/' and expression[curent_left] != '+' and expression[curent_left] != '-':
            left = expression[curent_left] + left
            curent_left -= 1
        else:
            break
    return float(left), curent_left


def CheckRight(i, expression):
    curent_right = i + 1
    right = ''
    while curent_right != len(expression):
        if expression[curent_right] != '*' and expression[curent_right] != '/' and expression[curent_right] != '+' and expression[curent_right] != '-':
            right = right + expression[curent_right]
            curent_right += 1
        else:
            break
    return float(right), curent_right


def Operation(Ch_oper, expression):
    result = 0
    while Ch_oper in expression:
        for i in range(len(expression)):
            if expression[i] == Ch_oper:
                left_n, curent_left = CheckLeft(i, expression)
                right_n, curent_right = CheckRight(i, expression)

                if Ch_oper == '*':
                    result += left_n * right_n

                elif Ch_oper == '/':
                    result += left_n / right_n

                elif Ch_oper == '+':
                    result += left_n + right_n

                elif Ch_oper == '-':
                    result += left_n - right_n

                expression = expression[:curent_left+1] + str(result) + expression[curent_right:]
                result = 0
                print(expression)
                break
    return expression


def Calculator(expression):
    expression = Operation('*', expression)
    expression = Operation('/', expression)
    expression = Operation('-', expression)
    expression = Operation('+', expression)


sleep(2)
print('\nРешение')
expression = input('Введите выражение, например 4+5*3: ')
Calculator(expression)
print('___________________________________________________________________________________')

