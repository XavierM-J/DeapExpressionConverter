import expression

example1 = "mul(cos(add(add(1,2),3)),add(4,5))"
example2 = "mul(1,add(3,protected_log(sub(mul(1,cos(1)),sin(1)))))"

print(expression.get_result_expression(example1))
print(expression.get_result_expression(example2))

