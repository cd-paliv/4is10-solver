from itertools import permutations, product
import operator
import math

def solve_4_equals_10(numbers, operations, allow_parentheses):
    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    numbers_permutations = permutations(numbers)
    for numbers in numbers_permutations:
        operations_combinations = product(operations, repeat=3)
        for ops_combination in operations_combinations: 
            expressions = generate_expressions(numbers, ops_combination, allow_parentheses)
            for expression in expressions:
                try:
                    if math.isclose(eval(expression), 10, rel_tol=1e-9):
                        return expression
                except ZeroDivisionError:
                    continue
    return "No solution found"

def generate_expressions(numbers, operations, allow_parentheses=True):
    if len(numbers) == 1:
        return [str(numbers[0])]

    expressions = []

    for i in range(len(numbers) - 1):
        left_numbers = numbers[:i + 1]
        right_numbers = numbers[i + 1:]

        for op in operations:
            left_expressions = generate_expressions(left_numbers, operations, allow_parentheses)
            right_expressions = generate_expressions(right_numbers, operations, allow_parentheses)

            for left_exp in left_expressions:
                for right_exp in right_expressions:
                    if allow_parentheses:
                        expressions.append(f"({left_exp} {op} {right_exp})")
                    expressions.append(f"{left_exp} {op} {right_exp}")

    return expressions



def main():
    while True:
        try:
            user_input = input("Enter the numbers separated by spaces (leave empty to exit): ")
            if not user_input:
                break
            numbers = list(map(float, user_input.split()))
            operations_input = input("Enter operations separated by spaces (or enter for default): ")
            operations = operations_input.split() if operations_input else ['+', '-', '*', '/']
            allow_parentheses = input("Allow parentheses? (press enter for yes/any other key for no): ").strip() == ''
            solution = solve_4_equals_10(numbers, operations, allow_parentheses)
            print("")
            print("Solution:", solution)
            print("")
            print("-------------------------------------------------------------")
        except ValueError:
            print("Invalid input. Please enter valid numbers and operations.")

if __name__ == "__main__":
    main()
