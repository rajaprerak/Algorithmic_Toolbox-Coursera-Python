def fibonacci_number(array,n):
    array[0] = 0;
    array[1] = 1;

    for i in range(2, n + 1):
        array[i] = (array[i - 1] + array[i - 2]) % 10;

    return array;

def last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to):
    array = [0]*61

    fibo_array_last_digit = fibonacci_number(array, 60)

    input_from_new = input_from % 60
    input_to_new = input_to % 60

    if input_from_new<input_to_new:
        array_new = fibo_array_last_digit[input_from_new:input_to_new+1]
        array_sum = sum(array_new)
    else:
        array_new1 = fibo_array_last_digit[input_from_new:61]
        array_new2 =fibo_array_last_digit[:input_to_new+1]
        array_sum = sum(array_new1) + sum(array_new2)

    return array_sum % 10

if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))
