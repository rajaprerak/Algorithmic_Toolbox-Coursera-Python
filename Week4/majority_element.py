def majority_element(elements):
    assert len(elements) <= 10 ** 5
    track_count = {}
    for each in elements:
        if each in track_count:
            track_count[each] += 1
        else:
            track_count[each] = 1

    for value in track_count.values():
        if value > len(elements) / 2:
            return 1
        else:
            temp = 0
    if temp == 0:
        return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
