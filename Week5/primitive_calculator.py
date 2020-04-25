# python3

import sys
def compute_operations(n):
    assert 1 <= n <= 10 ** 6
    if n == 1:
        return [1]
    ops = min_ops(n)
    return construct_min_list(n, ops)

def construct_min_list(n, ops):
    sequence = []
    while n > 0:
        sequence.append(n)
        if n % 2 != 0 and n % 3 != 0:
            n = n - 1
        elif n % 2 == 0 and n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            if ops[n-1] < ops[n//2]:
                n = n-1
            else:
                n = n // 2
        elif n % 3 == 0:
            if ops[n-1] < ops[n//3]:
                n = n-1
            else:
                n = n // 3
    return sequence

def min_ops(n):
    result = []
    for i in range(0, n+1):
        result.append(0)
    for i in range(2, n+1):
        min1 = result[i-1]
        min2 = sys.maxsize
        min3 = sys.maxsize
        if i % 2 == 0:
            min2 = result[int(i/2)]
        if i % 3 == 0:
            min3 = result[int(i/3)]
        minOp = min(min1, min2, min3)

        result[i] = minOp + 1

    return result



if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    output_sequence_output = output_sequence[::-1]
    print(output_sequence_output[:len(output_sequence)-1])
