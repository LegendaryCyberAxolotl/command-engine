def run(command, options, args, context, engine):
    sign = ""

    if options is not None:
        if options == ['-', 'd']: context.setDEFAULT_SIGN(); return
        sign += '-'

    if options:
        for item in options:
            sign += str(item)
    if args:
        for item in args:
            sign += str(item)
        
    if len(sign) < 1:
        raise ValueError(f"Sign cannot be empty")

    context.setSIGN(sign)