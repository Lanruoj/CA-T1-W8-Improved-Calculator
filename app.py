from pip import main


def _get_number(index):
    number = float(input(f"Number {index}: "))
    return number


def _get_goal():
    print("""
    Options:
    - "add"
    - "subtract"
    - "multiply"
    - "divide"
    - "check factors"
    """)
    user_input = input("What would you like to do with these numbers?:  ")
    return user_input

def _factor_check(first_number, second_number):
    if first_number == 0:
        return "Bad input"
    elif (first_number%second_number) == 0:
        return "True" 
    else:
        return "False" 

def _print_result(first_number, second_number, operation, result):
    print(f"{first_number} {operation} {second_number} = {result}")

def main_program():
    print("Hi, welcome to the calculator program! :-)")

    first_input = _get_number(1)
    second_input = _get_number(2)

    goal = _get_goal()

    if goal == "add":
        result = first_input + second_input
    elif goal == "subtract":
        result = first_input - second_input
    elif goal == "multiply":
        result = first_input * second_input
    elif goal == "divide":
        result = first_input / second_input
    elif goal == "check factors":
        result = _factor_check(first_input, second_input)
    else:
        result = "Invalid goal"
    
    _print_result(first_input, second_input, goal, result)

main_program()