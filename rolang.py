import sys

class SimpleInterpreter:
    def __init__(self):
        self.variables = {}

    def run(self, code):
        lines = code.split('\n')
        for line in lines:
            self.execute(line)

    def execute(self, line):
        tokens = line.split()

        if len(tokens) == 0:
            return

        if tokens[0] == "PRINT":
            if len(tokens) >= 2:
                expressions = ' '.join(tokens[1:])
                result = self.evaluate_expression(expressions)
                print(result)
            else:
                print("PRINT statement requires an expression.")

        elif tokens[0] == "USUT":
            if len(tokens) >= 2:
                variable_name = tokens[1]
                prompt = ' '.join(tokens[2:])
                user_input = input(f"{prompt} ")
                self.variables[variable_name] = user_input
            else:
                print("USUT statement requires a variable name.")
        elif tokens[0] == "IF":
            if len(tokens) >= 4 and tokens[2] == "==":
                    if tokens[1] not in self.variables:
                        print(f"Variable {tokens[1]} is not initialized.")
                        return

                    condition_tokens = tokens[1:4]
                    condition = self.evaluate_expression(condition_tokens)
                    if condition is None:
                        print("Invalid condition.")
                    elif condition:
                        block_code = ' '.join(tokens[4:])
                        self.execute(block_code)
                    else:
                        print("Condition not met.")

            else:
                print("Invalid IF statement:", ' '.join(tokens))
        elif len(tokens) >= 3 and tokens[1] == "=":
            variable_name = tokens[0]
            expression = ' '.join(tokens[2:])
            result = self.evaluate_expression(expression)
            self.variables[variable_name] = result
        else:
            print("Invalid statement:", line)

    def evaluate_expression(self, expression):
        try:
            return eval(expression, {}, self.variables)
        except Exception as e:
            print(f"Error evaluating expression: {e}")
            return None

def run_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            code = file.read()
            interpreter = SimpleInterpreter()
            interpreter.run(code)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error running code from file: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        run_from_file(file_path)
    else:
        print("Usage: python interpreter.py <file_path>")
