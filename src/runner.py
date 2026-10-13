from pathlib import Path
import importlib

class Runner:
    def __init__(self):
        self.ROOT = Path(__file__).resolve().parent.parent
        self.PATH = self.ROOT / "src" / "commands"

    def run(self, command, options, args, context, engine):
        command_file = self.PATH / f"{command}.py"
        
        if not command_file.exists():
            raise FileNotFoundError(f"Command '{command}' not found.")

        module = importlib.import_module(f"commands.{command}")
        func = getattr(module, "run")

        func(command, options, args, context, engine)