import sys

def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    value = []
    for i in range(len(weights)):
        value.append((prices[i] / weights[i], i))
    value = [list(i) for i in value]
    value = sorted(value, key=lambda x: x[0], reverse=True)

    total_weight = 0
    output_answer = 0
    for item in value:
        if capacity - total_weight >= weights[item[1]]:
            total_weight = total_weight + weights[item[1]]
            output_answer = output_answer + prices[item[1]]
        else:
            remaining_capacity = capacity - total_weight
            output_capacity = (remaining_capacity * prices[item[1]])/weights[item[1]]
            output_answer = output_answer + output_capacity
            break

    return output_answer


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
