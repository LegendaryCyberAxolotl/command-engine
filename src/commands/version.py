def run(command, options, args, context, engine):
    if options is not None:
        raise ValueError(f"Command {command} does not have any options")

    if len(args) != 0:
        raise ValueError(f"No arguments expected")

    print(context.VERSION)