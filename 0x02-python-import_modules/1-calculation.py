#!/usr/bin/python3

import calculator_1 as calc

def calc_results():

	a = 10
	b = 5

	sum_result = calc.add(a, b)
	diff_result = calc.sub(a, b)
	prod_result = calc.mul(a, b)
	quot_result = calc.div(a, b)

	print(f"Sum: {sum_result}")
	print(f"Difference: {diff_result}")
	print(f"Product: {prod_result}")
	print(f"Quotient: {quot_result}")

if __name__ == "__main__":
	calc_results()
