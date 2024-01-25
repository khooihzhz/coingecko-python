def process_function_args(func):
    def wrapper(*args, **kwargs):
        args = [process_arg(arg) for arg in args]

        for key in kwargs:
            kwargs[key] = process_arg(kwargs[key])

        return func(*args, **kwargs)

    return wrapper

def process_arg(arg):
    if isinstance(arg, list):
        arg = list_to_string(arg)
    elif isinstance(arg, bool):
        arg = bool_to_string(arg)

    return arg

def list_to_string(list):
    return ','.join(list)

def bool_to_string(bool):
    return str(bool).lower()

