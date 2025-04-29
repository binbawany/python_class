def count_up_to_list(max):
    numbers = []
    count = 1
    while count <= max:
        numbers.append(count)
        count += 1
    return numbers

for number in count_up_to_list(5):
    print(number)


def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

for number in count_up_to(5):
    print(number) # Outputs: 1 2 3 4 5    