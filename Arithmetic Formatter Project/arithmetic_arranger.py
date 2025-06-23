def arithmetic_arranger(problems, show_answers=False):
    first_values = ''
    second_values = ''
    line_values = ''
    result_values = ''
    error = ''
    final_str = ''

    if len(problems) > 5:
        error = 'Error: Too many problems.'
    else:
        for problem in problems:
            items = problem.split(' ')
            line = ''
            result = 0

            try:
                if items[1] == '+':
                    result = int(items[0]) + int(items[2])
                elif items[1] == '-':
                    result = int(items[0]) - int(items[2])
                else:
                    error = "Error: Operator must be '+' or '-'."
                    break
            except ValueError:
                error = 'Error: Numbers must only contain digits.'
                break

            tab = ''
            if first_values != '':
                tab = '    '
            
            if len(items[0]) > 4 or len(items[2]) > 4:
                error = 'Error: Numbers cannot be more than four digits.'
                break

            n_chars = max(len(items[0]), len(items[2]))
            first = tab + items[0].rjust(n_chars + 2, ' ')
            second = tab + items[1] + items[2].rjust(n_chars + 1, ' ')
            line = tab + line.rjust(n_chars + 2, '-')
            res = tab + str(result).rjust(n_chars + 2, ' ')

            first_values += first
            second_values += second
            line_values += line
            result_values += res

        final_str = first_values + '\n' + second_values + '\n' + line_values
        if show_answers:
            final_str += '\n' + result_values

    if error != '':
        return error
    else:
        return final_str