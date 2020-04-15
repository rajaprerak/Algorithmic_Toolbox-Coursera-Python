def fibonacci_number(n):
    assert 0 <= n <= 45
    array = []
    array.append(0)
    array.append(1)
    if n == 0:
        return array[0]
    if n == 1:
        return array[1]

    for i in range(2,n+1):
        array.append(array[i-1] + array[i-2])
    return array[n]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
