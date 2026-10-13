def run(command, options, args, context, engine):
    ALLOWED_OPTIONS = {'c', 'l', 'd'}
    unknown = set(options or []) - ALLOWED_OPTIONS
    if unknown:
        raise ValueError(f"Unexpected options provided for the '{command}' command: {', '.join(unknown)}")
    
    if len(args) > 2:
        raise ValueError(f"Too many arguments provided for the '{command}' command. Expected at most 2 arguments.")

    variables = context.variables
    var_name = args[0] if args else None
    var_value = args[1] if len(args) > 1 else None

    def default():
        if var_name is None:
            raise ValueError("Variable name is required.")
        variables[var_name] = var_value
        print(f"Variable '{var_name}' set to '{var_value}'.")

    def delete():
        if var_name is None:
            raise ValueError("Variable name is required.")
        if var_name not in variables:
            raise ValueError(f"Variable '{var_name}' does not exist.")
        
        del variables[var_name]
        print(f"Variable '{var_name}' deleted.")
        
    def list_vars():
        if var_name:
            if var_name not in variables:
                raise ValueError(f"Variable '{var_name}' does not exist.")
            
            print(f"{var_name}: {variables[var_name]}")
            return
            
        if variables:
            print("Current variables:")
            for name, value in variables.items():
                print(f"{name}: {value}")
        else:
            print("")

    def clear_vars():
        if not variables:
            print("No variables to clear.")
            return
        
        variables.clear()
        print("All variables cleared.")

    if options is None:
        default()
    elif options == ['d']:
        delete()
    elif options == ['l']:
        list_vars()
    elif options == ['c']:
        clear_vars()
    else:
        raise ValueError(f"Unexpected options provided for the '{command}' command.")