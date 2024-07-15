import random

def list_shuffle(li):
    n = len(li)
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)
        li[i], li[j] = li[j], li[i]
    return li

def is_sorted(li):
    for i in range(len(li) - 1):
        if li[i] > li[i + 1]:
            return False
    return True

def monkey_sort(li):
    while is_sorted(li) == False:
        li = list_shuffle(li)
    return li

# Example usage:
li = [3, 1, 4, 1, 5, 9, 2, 6, 5]
sorted_li = monkey_sort(li)
print(sorted_li)