from decorators import is_admin, error_handler, check_types, cache_results, rate_limiter

# Test is_admin
@is_admin
def show_customer_receipt(user_type: str):
    print("Showing customer receipt...")

# Test error_handler
@error_handler
def risky_function(data):
    print(data['key'])

# Test check_types
@check_types
def add(a: int, b: int) -> int:
    return a + b

# Test cache_results
@cache_results
def expensive_operation(n):
    print(f"Executing expensive operation for {n}")
    return n * 2

# Test rate_limiter
@rate_limiter(3)  
def limited_function():
    print("Function executed.")

# TEST is_admin
if __name__ == "__main__":
    print("\n=== TEST is_admin ===")
    try:
        show_customer_receipt(user_type='user')
    except ValueError as e:
        print(e)

    show_customer_receipt(user_type='admin')

    print("\n=== Тест error_handler ===")
    risky_function({'foo': 'bar'})
    risky_function({'key': 'bar'})

    print("\n=== Тест check_types ===")
    print(add(1, 2))
    try:
        add("1", "2")
    except TypeError as e:
        print(e)

    print("\n=== TEST cache_results ===")
    print(expensive_operation(5))
    print(expensive_operation(5))  

    print("\n=== TEST rate_limiter ===")
    limited_function()
    limited_function()
    limited_function()
    try:
        limited_function()
    except ValueError as e:
        print(e)
