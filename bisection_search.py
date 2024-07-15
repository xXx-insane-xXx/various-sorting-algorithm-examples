def bisection_search(li, target):

    low = 0
    high = len(li) - 1

    while low <= high:
        mp = (low + high) // 2
        if li[mp] == target:
            return True
        elif li[mp] > target:
            high = mp - 1
        else:
            low = mp + 1

    return False