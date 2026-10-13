from runner import Runner
from parser import Parser
from context import Context

class Engine:
    def __init__(self):
        self.runner = Runner()
        self.parser = Parser()
        self.context = Context()

    def execute(self, line: str) -> None:
        command, options, args = self.parser.parse(line)
        self.context.history.append(line)
        self.runner.run(command, options, args, self.context, self)

    def start(self):
        while self.context.running:
            try:
                self.execute(input(self.context.SIGN))
            except Exception as e:
                print(f"Error: {e}")