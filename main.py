import art
def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiple(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
print(art.logo)
new_calculator = True
while new_calculator:
    first_number = int(input("Enter the first number:"))
    container = []
    want_to_continue = True
    while want_to_continue:
        function_storage = {"+" : add ,"-": subtract ,"*": multiple,"/": divide}
        operation = input(" + \n - \n * \n /\nEnter the operation you want to perform:")
        second_number = int(input("Enter the second number: "))
        calculation_operation = function_storage[operation](first_number,second_number)
        container.append(calculation_operation)
        print(calculation_operation)
        first_number = container[0]
        container.pop(0)
        user_choice = input("If you want to continue with this value, type 'y'.If you want to new calculator type 'n': ")
        if user_choice == "n":
            want_to_continue = False
