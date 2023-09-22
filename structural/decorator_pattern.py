from functools import wraps


def make_blink(function):
    """Definition of the decorator"""

    # This makes the decorator transparent in terms of its name and docstring
    @wraps(function)

    # Define the inner function
    def decorator():
        # Grab the return value of the function being decorated
        ret = function()

        # Add functionality to the function being decorated
        return f"<blink>{ret}</blink>"

    return decorator


# Apply the decorator here


@make_blink
def hello_world():
    return "Hello World!"


print(hello_world())
