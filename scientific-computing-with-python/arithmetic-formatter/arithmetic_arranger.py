def arithmetic_arranger(problems, display_answers=False):

    if len(problems) > 5:
        return "Error: Too many problems."

    top_line = bottom_line = dashes = results = ""

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."

        left, operator, right = parts

        # Validate the operator
        if operator not in "+-":
            return "Error: Operator must be '+' or '-'."

        # Validate operands are digits and not too long
        if not (left.isdigit() and right.isdigit()):
            return "Error: Numbers must only contain digits."
        if len(left) > 4 or len(right) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Formatting each problem
        width = max(len(left), len(right)) + 2
        top = f"{left:>{width}}"
        bottom = f"{operator} {right:>{width-2}}"
        dash = "-" * width
        result = ""  # Initialize result
        if display_answers:
            answer = eval(problem.replace(' ', ''))
            result = f"{answer:>{width}}"

        # Building the final output
        space = "    "  # 4 spaces between problems
        top_line += f"{top}{space}"
        bottom_line += f"{bottom}{space}"
        dashes += f"{dash}{space}"
        if display_answers:
            results += f"{result}{space}"

    arranged_problems = f"{top_line.rstrip()}\n{bottom_line.rstrip()}\n{dashes.rstrip()}"
    if display_answers:
        arranged_problems += f"\n{results.rstrip()}"

    return arranged_problems
