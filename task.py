def get_banknotes_from_atm(amount: float, banknotes: list) -> list:
    """Function that returns a list of banknotes the user receives from the amount
    inputted from list witch contains the banknotes inside in atm, the smallest amount of banknotes possible
    """
    result = []
    banknotes.sort(reverse=True)
    for i in range(len(banknotes)):
        if sum(result) <= amount:
            result.append(max(banknotes))
        if sum(result) > amount:
            result.pop()
            banknotes.remove(max(banknotes))
        if sum(result) < amount:
            result.append(max(banknotes))
    if sum(result) != amount:
        left_over_banknote = amount - sum(result)
        if result.count(max(result)) != 1 and min(banknotes) != left_over_banknote:
            result.remove(max(result))
        difference = amount - sum(result)
        for i in range(int(difference / max(banknotes))):
            result.append(max(banknotes))
    if sum(result) == amount:
        return result
    else:
        return False


print(get_banknotes_from_atm(13, [5, 2, 1]))
print(get_banknotes_from_atm(13, [1, 10]))
print(get_banknotes_from_atm(13, [5, 2]))
print(get_banknotes_from_atm(11.5, [0.5, 1, 10]))
print(get_banknotes_from_atm(11, [5, 2]))
print(get_banknotes_from_atm(14, [5, 2]))


def test_get_banknotes_from_atm():
    assert (get_banknotes_from_atm(13, [1, 2, 5]) == [5, 5, 2, 1])
    assert (get_banknotes_from_atm(13, [1, 10]) == [10, 1, 1, 1])
    assert (get_banknotes_from_atm(13, [2, 5]) == [5, 2, 2, 2, 2])
    assert (get_banknotes_from_atm(11.5, [0.5, 1, 10]) == [10, 1, 0.5])
    assert (get_banknotes_from_atm(14, [5, 2]) == [5, 5, 2, 2])
    print("All test pass")


test_get_banknotes_from_atm()
