def run(command, options, args, context, engine):
    if options is not None:
        raise ValueError(f"Command {command} does not have any options.")
        
    if len(args) != 1:
        raise ValueError(f"Expected exactly 1 argument.")

    context.setSIGN(args[0])