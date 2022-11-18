from cie_builtins import *
from re import search

REMOVE = '''ENDWHILE
ENDFUNCTION
ENDPROCEDURE
NEXT
DECLARE
ENDIF'''.splitlines()

CONVERT_MAP = {'←':'=', '&':'+', '<>':'!=', ' THEN':':', 'TRUE':'True', 'FALSE': 'False', 'CALL ':'',
               'INTEGER':'int', 'BOOLEAN':'bool', 'CHARACTER':'str', 'STRING':'str', 'RETURNS':'->',
                'REAL':'float', 'PROCEDURE':'def', 'FUNCTION':'def'}

TEST_CASE_DELIM = "\n\n"

CONVERT_UPPER = '''AND
FOR
NOT
IF
ELSE
RETURN
OR
WHILE'''.splitlines()

file_count = 1

fn_map = {}

def check_syntax(pseudocode):
    '''Check pseudocode syntax and report syntax errors'''
    pass

def get_indent_width(line):
    indent = ""
    for char in line:
        if char in "\t ":
            indent += char
        else:
            break
    return indent

def convert(pseudocode):
    '''Convert pseudocode into Python'''
    control_stack = []
    file_count = 0

    # remove declarations and end keywords
    python = [line for line in pseudocode.splitlines() if not(any(line.strip().startswith(rem) for rem in REMOVE))]
    python = "\n".join(python)
    # correct direct replacements
    for pseu_token, py_token in CONVERT_MAP.items():
        python = python.replace(pseu_token, py_token)

    # correct UPPERCASE keywords
    for kw in CONVERT_UPPER:
        python = python.replace(kw, kw.lower())

    new_python = ""
    for line_no, line in enumerate(python.splitlines()):
        indent = get_indent_width(line)
        s_line = line.strip()

        # convert definite iteration expressions
        if s_line.startswith("for"):
            var, iter_exp = line.replace("for ", "").split(" = ")
            start, stop = iter_exp.split(" TO ")
            step = None
            if "STEP" in stop:
                stop, step = stop.split(" STEP ")
                if stop.replace("-", "").isdigit():
                    stop = int(stop) + 1
            line = f"{indent}for {var} in range({start}, {stop}"
            line +=  "):" if step is None else f", {step}):"

        # convert pre-condition loop statements
        if any(s_line.startswith(kw) for kw in ["while","def","else"]):
            line = indent+line.strip()+":"

        if s_line.startswith("REPEAT"):
            line = f"{indent}while True:"

        if s_line.startswith("UNTIL"):
            line = line.replace("UNTIL", "\tif") + f":\n{indent}\t\tbreak"

        if s_line.startswith("OPENFILE"):
            mode = s_line.split()[-1][0].lower()
            quote = '"' if '"' in s_line else "'"
            fn = f'{s_line.split(quote)[1]}'
            file_var = f"file{file_count}"
            fn_map[fn] = file_var
            file_count += 1
            line = f"{indent}{file_var} = open({fn}, '{mode}')"

        if s_line.startswith("CLOSEFILE"):
            fn = s_line.replace("CLOSEFILE ", "")[1:-1]
            line = f"{indent}{fn_map[fn]}.close()"

        if s_line.startswith("READLINE"):
            fn, line_var = s_line.replace("READLINE ", "").split(" ") # won't work if spaces in fns
            fn = fn[1:-2]
            line = f"{indent}{line_var} = {fn_map[fn]}.readline()"

        if s_line.startswith("WRITELINE"):
            fn, write_data = s_line.replace("WRITELINE ", "").split(" ")  # won't work if spaces in fns
            fn = fn[1:-2]
            line = f"{indent}{fn_map[fn]}.write({write_data}+'\\n')"

        if s_line.startswith("INPUT"):
            inp, var = s_line.split()
            line = f"{indent}{var} = input()"

        if s_line.startswith("OUTPUT"):
            exp = s_line.replace("OUTPUT ", "")
            line = f"{indent}print({exp})"



        new_python += line
        new_python += "\n"


    return new_python


if __name__ == "__main__":

    with open("test_cases.txt", encoding="utf8") as f:
        tests = f.read().split(TEST_CASE_DELIM)

    for test in tests:
        print(convert(test))