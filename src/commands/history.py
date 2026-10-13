def run(command, options, args, context, engine):
    ALLOWED_OPTIONS = {'c', 'i', 'n', 'l'}
    unknown = set(options or []) - ALLOWED_OPTIONS
    if unknown:
        raise ValueError(f"Unexpected options provided for the '{command}' command: {', '.join(unknown)}")
    
    if not context.history:
        print("No commands in history.")
        return
    
    if len(args) > 1:
        raise ValueError(f"Too many arguments provided for the '{command}' command. Expected at most 1 argument.")

    if len(args) == 1:
        try:
            index = int(args[0])
        except ValueError:
            raise ValueError(f"Invalid argument '{args[0]}'. Expected an integer index.")

    if options is None:
        if len(args) != 0:
            raise ValueError(f"No arguments expected with no options.")

        for i, cmd in enumerate(context.history):
            print(f"{i + 1}: {cmd}")

    elif options == ['c']:
        if len(args) != 0:
            raise ValueError(f"No arguments expected with the 'c' option.")

        context.history.clear()
        print("Command history cleared.")

    elif options == ['i']:
        if len(args) == 0:
            raise ValueError(f"Expected 1 argument with the 'i' option.")

        if index < 1 or index > len(context.history):
            raise ValueError(f"Index {index} is out of range. Valid range is 1 to {len(context.history)}.")

        print(f"{index}: {context.history[index - 1]}")

    elif options == ['n']:
        if len(args) == 0:
            raise ValueError(f"Expected 1 argument with the 'n' option.")

        if index < 1:
            raise ValueError(f"The number must be at least 1.")

        if index > len(context.history):
            index = len(context.history)
        

        for i in range(index):
            print(f"{i + 1}: {context.history[i]}")

    elif sorted(options) == ['l']:
        if len(args) == 0:
            raise ValueError(f"Expected at least 1 argument with the 'l' option.")
    
        if index < 1:
            raise ValueError(f"The number must be at least 1.")

        if index > len(context.history):
            index = len(context.history)

        reverse_history = context.history[::-1]
        for i in range(index):
            print(f"{i + 1}: {reverse_history[i]}")

    else:
        raise ValueError(f"Unexpected options provided for the '{command}' command.")