def display():
    return "Display function executed"

def wrapper_function(original_function):
    print(f"Wrapper executed this before {original_function.__name__}")
    return original_function()

# Manually apply the 'wrapping' behavior
wrapped_display = wrapper_function(display)
print(wrapped_display)


def decorator_function(original_function):
    def wrapper_function():
        print(f"Wrapper executed this before {original_function._name_}")
        return original_function()
    return wrapper_function

@decorator_function
def display():
    return "Display function executed"

print(display())