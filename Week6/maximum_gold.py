from sys import stdin


def maximum_gold(capacity, weights):
    assert 1 <= capacity <= 10 ** 4
    assert 1 <= len(weights) <= 10 ** 3
    assert all(1 <= w <= 10 ** 5 for w in weights)
    n = len(weights)
    dp_array = [[0] * (capacity + 1) for i in range(n)]
    for i in range(n):
        for j in range(capacity + 1):
            if i == 0:
                if j >= weights[i]:
                    dp_array[i][j] = weights[i]
            else:
                if j >= weights[i]:
                    dp_array[i][j] = max(weights[i] + dp_array[i - 1][j - weights[i]], dp_array[i - 1][j])
                else:
                    dp_array[i][j] = dp_array[i - 1][j]
    return dp_array[n - 1][capacity]


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n
    print(maximum_gold(input_capacity, input_weights))
