
def _get_number(index):
    number = float(input(f"Number {index}: "))
    return number


def _get_goal():
    goal_list = ["add", "subtract", "multiply", "divide", "check factors"
    ]
    print("Options:\n{goal_list}")
    user_input = input("What would you like to do with these numbers?:  ")
    if user_input in goal_list:
        return user_input
    else:
        return "Invalid goal"

#-------OPERATIONS-------#

def _factor_check(first_number, second_number):
    if first_number == 0:
        return "Bad input"
    elif not first_number % second_number:
        return "True"
    else:
        return "False" 

def _print_result(first_number, second_number, operation, result):
    print(f"{first_number} {operation} {second_number} = {result}")

def _add(first_number, second_number):
    return first_number + second_number

def _subtract(first_number, second_number):
    return first_number - second_number

def _multiply(first_number, second_number):
    return first_number / second_number

def _divide(first_number, second_number):
    return first_number / second_number

#-------------------------#

def main_program():
    print("Hi, welcome to the calculator program! :-)")

    first_input = _get_number(1)
    second_input = _get_number(2)

    goal = _get_goal()
    
    #STORE FUNCTION NAMES IN A DICT#
    operation_dict = {
        "add": _add,   # no () because only storing function name, not execution!
        "subtract": _subtract,
        "multiply": _multiply,
        "divide": _divide,
        "check factors": _factor_check
    }

    # if goal == "add":
    #     result = first_input + second_input
    # elif goal == "subtract":
    #     result = first_input - second_input
    # elif goal == "multiply":
    #     result = first_input * second_input
    # elif goal == "divide":
    #     result = first_input / second_input
    # elif goal == "check factors":
    #     result = _factor_check(first_input, second_input)
    # else:
    #     result = "Invalid goal"
    
    _print_result(first_input, second_input, goal, result)

main_program()