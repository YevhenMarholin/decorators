import inspect
from functools import wraps

def check_types(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()

        for param, value in bound_args.arguments.items():
            expected_type = sig.parameters[param].annotation
            if expected_type is not inspect.Parameter.empty and not isinstance(value, expected_type):
                raise TypeError(f"Argument {param} must be {expected_type.__name__}, not {type(value).__name__}")

        result = func(*args, **kwargs)
        return_type = sig.return_annotation

        if return_type is not inspect.Signature.empty and not isinstance(result, return_type):
            raise TypeError(f"Return value must be {return_type.__name__}, not {type(result).__name__}")

        return result
    return wrapper
