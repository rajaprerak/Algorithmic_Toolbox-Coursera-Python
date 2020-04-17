def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d
    refill = 0
    stops.append(d)
    miles = m
    previous = 0
    for stop in range(len(stops)):
        if stops[stop] - previous > m:
            return -1
        else:
            previous = stops[stop]

        if stops[stop] > miles:
            miles = m + stops[stop-1]
            refill = refill + 1

    return refill


if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
