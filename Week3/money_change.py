def money_change(money):
    assert 0 <= money <= 10 ** 3
    no_of_fives = 0
    no_of_ones = 0
    no_of_tens = money//10
    money_left = money - no_of_tens*10
    if money_left > 0:
        no_of_fives = money_left // 5
        money_remaining = money_left - no_of_fives*5
        if money_remaining > 0:
            no_of_ones = money_remaining

    total_coins = no_of_tens + no_of_fives + no_of_ones

    return total_coins


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
