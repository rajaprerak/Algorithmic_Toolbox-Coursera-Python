def pisano_period(m):
    previous = 0
    current = 1
    for i in range(m * m + 1):
        previous, current = current, (previous + current) % m
        if previous == 0 and current == 1:
            return i + 1

def fibonacci_number(n):
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

def fibonacci_number_again(n,m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3
    rem = n % pisano_period(m)
    return fibonacci_number(rem) % m

if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
