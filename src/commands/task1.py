def task1():
    print("Hi!")

def run(command, options, args, context, engine):
    if options or args:
        raise ValueError(f"Options and arguments are not supported for the '{command}' command.")

    task1()