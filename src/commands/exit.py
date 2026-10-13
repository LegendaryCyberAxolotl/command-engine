def run(command, options, args, context, engine):
    if args or options:
        raise ValueError(f"Options and arguments are not supported for the '{command}' command.")

    print("Exiting the program...")
    context.running = False