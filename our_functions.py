def describe_pet(name, **animal):
    print(f"{name} is a {animal.get('animal_type', 'Dog')} and is {animal.get('age', 7)} years old.")



#describe_pet("Lasi") 

def is_prime(num):
    if num < 2:
        return False
    for x in range(2, int(num ** 0.5) + 1):
        if num % x == 0:
            return False
    return True

#print(is_prime(9))


def calculate_area(radius):
    pi = 3.14
    area = pi * radius ** 2
    return area

def print_area(radius):
    area = calculate_area(radius)
    print(f"the area of the circle is {area}")

print_area(100)

