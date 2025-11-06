def converter_expression(expression, to_format="postfix"):
    if to_format == "postfix":
        tokens = expression.split()
        stack = []
        result = []
        for token in tokens:
            if token.isdigit():
                result.append(token)
            elif token in ['+', '-', '*', '/']:
                stack.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    result.append(stack.pop())
                stack.pop()

        while stack:
            result.append(stack.pop())

        return " ".join(result)

    else:
        return "Конвертация в инфиксную запись пока не реализована"

expressions = [
    "2 + 3",
    "( 3 + 4 ) * 5",
    "1 + 2 * 3"
]

for expr in expressions:
    converted = converter_expression(expr, "postfix")
    print(f"Инфиксная: {expr} -> Постфиксную: {converted}")