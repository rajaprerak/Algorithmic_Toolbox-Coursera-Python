def binary_search(keys, query):
    assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
    assert 1 <= len(keys) <= 3 * 10 ** 4
    start = 0
    end = len(keys) - 1
    while start < end:
        mid = (start + end) // 2
        if keys[mid] == query:
            return mid
        if keys[mid] < query:
            start = mid + 1
        if keys[mid] > query:
            end = mid - 1
    return -1


if __name__ == '__main__':
    input_keys = list(map(int, input().split()))[1:]
    input_queries = list(map(int, input().split()))[1:]

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
