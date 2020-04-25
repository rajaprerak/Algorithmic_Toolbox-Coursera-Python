# python3


def lcs2(first_sequence, second_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100

    len_first = len(first_sequence)
    len_second = len(second_sequence)
    dp_array = [[0] * (len_second + 1) for i in range(len_first + 1)]

    for i in range(len_first + 1):
        for j in range(len_second + 1):

            if i == 0 or j == 0:
                dp_array[i][j] = 0
            elif first_sequence[i - 1] == second_sequence[j - 1]:
                dp_array[i][j] = dp_array[i - 1][j - 1] + 1
            else:
                dp_array[i][j] = max(dp_array[i - 1][j], dp_array[i][j - 1])

    return dp_array[len_first][len_second]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
