import math


def is_one_digit(number):
    if (number > -10) and (number < 10) and (isinstance(number, int)):
        return True
    else:
        return False


def check(num_1, num_2, operation):
    message = ""
    if is_one_digit(num_1) and is_one_digit(num_2):
        message += " ... lazy"
    if (num_1 == 1 or num_2 == 1) and operation == '*':
        message += " ... very lazy"
    if (num_1 == 0 or num_2 == 0) and operation in ('*', '+', '-'):
        message += " ... very, very lazy"
    if message != "":
        message = "You are" + message
        print(message)


def return_int_for_float(number):
    if abs(number) - math.floor(abs(number)) != 0:
        return number
    else:
        return math.floor(number)


messages = ("Are you sure? It is only one digit! (y / n)",
            "Don't be silly! It's just one number! Add to the memory? (y / n)",
            "Last chance! Do you really want to embarrass yourself? (y / n)")
memory = 0
while True:
    print("Enter an equation")
    number_1, operand, number_2 = input().split()
    if number_1 == 'M':
        number_1 = memory
    if number_2 == 'M':
        number_2 = memory
    try:
        number_1_float = float(number_1)
        number_2_float = float(number_2)
    except ValueError:
        print("Do you even know what numbers are? Stay focused!")
        continue
    else:
        if operand not in ('+', '-', '*', '/'):
            print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
            continue
        else:
            number_1_int = return_int_for_float(number_1_float)
            number_2_int = return_int_for_float(number_2_float)
            check(number_1_int, number_2_int, operand)
            if operand == '+':
                result = number_1_float + number_2_float
            elif operand == '-':
                result = number_1_float - number_2_float
            elif operand == '*':
                result = number_1_float * number_2_float
            else:
                if number_2_float == 0:
                    print("Yeah... division by zero. Smart move...")
                    continue
                else:
                    result = number_1_float / number_2_float
            print(result)
            result_int = return_int_for_float(result)
            answer = 'y'
            while answer != 'n':
                answer = input("Do you want to store the result? (y / n):")
                if answer == 'y':
                    if is_one_digit(result_int):
                        msg_index = 0
                        read_answer = 'y'
                        while read_answer != 'n':
                            read_answer = input(messages[msg_index])
                            if read_answer == 'y':
                                if msg_index < 2:
                                    msg_index += 1
                                    continue
                                else:
                                    memory = result
                                    answer = 'n'
                                    break
                            else:
                                if read_answer == 'n':
                                    answer = 'n'
                                    break
                                else:
                                    continue
                    else:
                        memory = result
                        break
                else:
                    if answer == 'n':
                        break
                    else:
                        continue
            choice = 'y'
            while choice != 'n':
                choice = input("Do you want to continue calculations? (y / n):")
                if choice == 'y':
                    break
                else:
                    if choice == 'n':
                        break
                    else:
                        continue
            if choice == 'y':
                continue
            else:
                break
