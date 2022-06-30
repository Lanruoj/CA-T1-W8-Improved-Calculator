def _get_number(index):
    number = float(input(f"Number {index}: "))
    return number

def _get_goal(goal_dict):
    
    print("Options:")
    print(list(goal_dict.keys()))
    user_input = input("What would you like to do with these numbers?: ")
    return user_input


def _print_result(first_number, second_number, operation, result):
    print(f"{first_number} {operation} {second_number} = {result}")

# ------------------------------------------------ # 

def _factor_check(first_number, second_number):
    if first_number == 0:
        return "Bad input"
    elif first_number % second_number == 0:
        return "True"
    else:
        return "False"

def _add(first_number, second_number):
    return first_number + second_number

def _subtract(first_number, second_number):
    return first_number - second_number

def _multiply(first_number, second_number):
    return first_number * second_number

def _divide(first_number, second_number):
    return first_number / second_number

def _to_the_power(first_number, second_number):
    return first_number ** second_number

operation_dict = {
    "add": _add,
    "subtract": _subtract,
    "multiply": _multiply,
    "divide": _divide,
    "check factors": _factor_check,
    "raise to the power": _to_the_power
}

# ---------------------------------- # 

def main_program(operations):
    print("Hi, welcome to the calculator program!")
    print ("Please input the numbers\n--------------")
    first_input = _get_number(1)
    second_input = _get_number(2)
    goal = _get_goal(operations)

    if not goal in operations:
        result = "invalid goal"
    else:
        result = operation_dict[goal](first_input, second_input)

    _print_result(first_input, second_input, goal, result)

main_program(operation_dict)