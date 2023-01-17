number = list(map(int, input("Введите через пробел последовательность чисел: ").split()))
element = int(input("Введите число: "))

def sort_number(number):
    for i in range(len(number)):
        for j in range(len(number) - i - 1):
            if number[j] > number[j + 1]:
                number[j], number[j + 1] = number[j + 1], number[j]
    return number

number_sort = sort_number(number)

def binary_search(number_sort, element, left= 0, right=len(number_sort)):
    if element <= min(number_sort) or element >= max(number_sort):
        return "Число не соотвествует критериям"
    elif left > right:
        return "Число отсутсвует"
    middle = (right + left) // 2
    if number_sort[middle] == element:
        return middle - 1
    elif element < number_sort[middle]:
        return binary_search(number_sort, element, left, middle - 1)
    else:
        return binary_search(number_sort, element, middle + 1, right)

print(binary_search(number_sort, element))


