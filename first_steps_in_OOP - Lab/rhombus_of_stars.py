def generate_pyramid(size: int, inverted: bool = False) -> list:
    steps = [i for i in range(1, size + 1)]
    if inverted:
        steps.reverse()
    return [' ' * (size - i) + '* ' * i for i in steps]


def generate_rhombus(size: int) -> list:
    result = generate_pyramid(size)
    result.extend(generate_pyramid(size, True)[1:])
    return result


n = int(input())
output = generate_rhombus(n)
print(*output, sep='\n')