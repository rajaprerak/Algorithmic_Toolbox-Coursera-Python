def largest_number(numbers):
    numbers = [int(a) for a in numbers]
    max_length = len(str(max(numbers)))
    new_numbers = []
    output = ""

    for i in numbers:
        extended_number = str(i) * max_length

        new_numbers.append((extended_number, i))
    new_numbers = sorted(new_numbers, key=lambda x: x[0], reverse=True)
    for each in new_numbers:
        output += str(each[1])

    return output


if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
