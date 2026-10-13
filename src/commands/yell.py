def run(command, options, args, context, engine):
    if not args:
        raise ValueError(f"No arguments provided for the '{command}' command.")
    
    message = ' '.join(args)
    print(message)