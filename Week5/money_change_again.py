def change(money):
    dp_array = [0] * (money + 1)
    dp_array[0] = 0
    coins = [1,3,4]
    for i in range(1, len(dp_array)):
        minimum_value = 100000
        for j in range(len(coins)):
            if i >= coins[j]:
                minimum_value = min(minimum_value, 1 + dp_array[i-coins[j]])
        dp_array[i] = minimum_value
    return dp_array[money]


if __name__ == '__main__':
    amount = int(input())
    print(change(amount))
