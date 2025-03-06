from functools import wraps

def is_admin(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if kwargs.get('user_type') != 'admin':
            raise ValueError("Permission denied")
        return func(*args, **kwargs)
    return wrapper
