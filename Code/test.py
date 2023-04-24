def process_array(n, arr, operations):
    for op in operations:
        l, r, t, x = op
        l -= 1
        r -= 1

        if t == '|':
            for i in range(l, r + 1):
                arr[i] |= x
        elif t == '&':
            for i in range(l, r + 1):
                arr[i] &= x
        elif t == '=':
            for i in range(l, r + 1):
                arr[i] = x

    return arr


def main():
    n = 4
    arr = [5, 4, 7, 4]
    m = 4
    l_values = [1, 2, 3, 2]
    r_values = [4, 3, 4, 2]
    operation_types = "=|&="
    x_values = [8, 3, 6, 2]

    operations = [(l_values[i], r_values[i], operation_types[i], x_values[i]) for i in range(m)]
    result = process_array(n, arr, operations)
    print(result)


if __name__ == "__main__":
    main()