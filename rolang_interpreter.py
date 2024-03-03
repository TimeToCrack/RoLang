class RolangInterpreter:
    print("RoLang 0.0.1 (C) Rochdi 2024-2024, All rights reserved!")
    print("Type \"HELP\" for a list of commands")
    def __init__(self):
        self.variables = {}

    def run(self):
        while True:
            code = input(">>> ")
            if code.lower() == "exit":
                break
            self.execute(code)

    def execute(self, code):
        tokens = code.split()

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

        elif len(tokens) >= 3 and tokens[1] == "=":
            variable_name = tokens[0]
            expression = ' '.join(tokens[2:])
            result = self.evaluate_expression(expression)
            self.variables[variable_name] = result

        elif tokens[0] == "HELP":
            print("PRINT = PRINTS TEXT.", "USUT = GIVES USER INPUT", "HELP = PRINTS THIS MESSAGE")

        elif tokens[0] == "IF":
            if len(tokens) >= 4 and tokens[2] == "==":
                condition = self.evaluate_expression(tokens[1])
                if condition:
                    block_code = ' '.join(tokens[3:])
                    self.execute(block_code)
                else:
                    print("Condition not met.")

            else:
                print("Invalid IF statement:", code)

        else:
            print("Invalid statement:", code)

    def evaluate_expression(self, expression):
        try:
            return eval(expression, {}, self.variables)
        except Exception as e:
            print(f"Error evaluating expression: {e}")
            return None

if __name__ == "__main__":
    interpreter = RolangInterpreter()
    interpreter.run()
