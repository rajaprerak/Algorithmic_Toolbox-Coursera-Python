def fibonacci_number(array,n):
    array[0] = 0;
    array[1] = 1;

    for i in range(2, n + 1):
        array[i] = (array[i - 1] + array[i - 2]) % 10;

    return array;

def last_digit_of_fibonacci_number(n):
    array = [0]*61

    fibo_array_last_digit = fibonacci_number(array, 60)

    return fibo_array_last_digit[n%60]

if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))
