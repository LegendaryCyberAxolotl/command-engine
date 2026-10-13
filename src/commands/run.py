def run(command, options, args, context, engine):
    if options is not None:
         raise ValueError(f"Command {command} does not have any options.")
    
    if len(args) < 1:
        raise ValueError(f"Expected path as an argument.")

    path = " ".join(args)

    try:
        with open(path, 'r', encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                engine.execute(line)
    except Exception as e:
        print(f"Error: {e}")