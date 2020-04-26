def partition3(arr, partitions):
    total_sum = 0
    n = len(arr)

    for i in range(n):
        total_sum += arr[i]
    if total_sum % partitions != 0:
        return 0

    part = [[True for i in range(n + 1)] for j in range(total_sum // partitions + 1)]

    for i in range(0, n + 1):
        part[0][i] = True
    for i in range(1, total_sum // partitions + 1):
        part[i][0] = False

    for i in range(1, total_sum // partitions + 1):
        for j in range(1, n + 1):
            part[i][j] = part[i][j - 1]
            if i >= arr[j - 1]:
                part[i][j] = (part[i][j] or part[i - arr[j - 1]][j - 1])

    if part[total_sum // partitions][n]:
        return 1
    else:
        return 0


if __name__ == '__main__':
    input_values = list(map(int, input().split()))
    no_of_partitions = int(input())
    print(partition3(input_values, no_of_partitions))
