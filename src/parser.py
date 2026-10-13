class Parser:
    def __init__(self):
        self.command_line = ""
        self.DELIMITER = ' '
        self.OPTION_PREFIX = '-'

    def parse(self, command_line):
        if command_line.startswith("#"):
            return "comment", [], []
        
        self.command_line = command_line.strip()
        if not self.command_line:
            raise ValueError("Command line cannot be empty.")

        tokens = self.command_line.split(self.DELIMITER)
        command = tokens[0]
        if len(tokens) == 1:
            return command, None, []
        
        if tokens[1].startswith(self.OPTION_PREFIX):
            options = tokens[1]
            options = options[1:]  # Remove the '-' prefix
            options = list(options)  # Convert to a list of individual option characters
        else:
            options = None

        end = next((i for i, t in enumerate(tokens) if t.startswith("#")), len(tokens))
        args = tokens[1:end] if options is None else tokens[2:end]
        return command, options, args