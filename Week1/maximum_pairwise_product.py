def max_pairwise_product(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)
    first = 0
    second = 0
    for i in range(len(numbers)):
        if numbers[i] > first:
            second = first
            first = numbers[i]

        elif numbers[i] > second:
            second = numbers[i]

    return first*second


if __name__ == '__main__':
    n = int(input())
    input_numbers = list(map(int, input().split()))
    assert len(input_numbers) == n
    print(max_pairwise_product(input_numbers))
