def intList():
    global num
    num = input('Введите произвольное количество целых чисел, используйте пробел в качестве разделителя - ')
    try:
        num = list(map(int, num.split()))
    except ValueError:
        print('\nПожалуйста, при вводе не используйте никаких символов, кроме цифр и пробела. Все числа должны быть целыми, ввод дробных чисел не допускается.\nПовторите ввод, соблюдая вышеописанные условия.')
        intList()
    return num

list_of_num = intList()

def isInt():
    global s_num
    s_num = input('Введите любое целое число - ')
    if s_num.isdigit():
        s_num = int(s_num)
    else:
        print('\nПожалуйста, при вводе не используйте никаких символов, кроме цифр.')
        isInt()
    return s_num

single_num = isInt()

def sort_(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = sort_(L[:middle])
        right = sort_(L[middle:])
        return merge(left, right)

def merge(left,right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

list_of_num = sort_(list_of_num)
print(f'\nОтсортированный в порядке возрастания список - {list_of_num}')

def search(array, element, left, right):
    if left > right:
            return False
    middle = (left + right) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return search(array, element, left, middle-1)
    else:
        return search(array, element, middle+1, right)

mid = search(list_of_num, single_num, 0, len(list_of_num)-1)
elem = list_of_num[mid-1]

if search(list_of_num, single_num, 0, len(list_of_num)-1) is not False:
    if mid == 0:
        print(f'\nВведёное вами число имеет минимальное значение, оно стоит на первом месте в списке.')
    else:
        print(f'\nИндекс ближайшего элемента, который меньше введённого вами числа - {list_of_num.index(elem)}, а сам элемент равняется {elem}.')
else:
    if single_num < list_of_num[0]:
        elem = list_of_num[0]
        print(f'\nВ списке нет введённого вами числа. Ближайший больший элемент является первым в списке и равняется {elem}, его индекс - {list_of_num.index(elem)}.')
    elif single_num > list_of_num[-1]:
        elem = list_of_num[-1]
        print(
            f'\nВ списке нет введённого вами числа. Ближайший меньший элемент является последним в списке и равняется {elem}, его индекс - {list_of_num.index(elem)}.')
    else:
        mid = (0 + len(list_of_num)-1) // 2
        i = mid
        j = mid + 1
        while not list_of_num[i] < single_num < list_of_num[j]:
            if single_num < list_of_num[mid]:
                i -= 1
                j -= 1
            else:
                i += 1
                j += 1
        else:
            print(f'\nВ списке нет введённого вами числа.\nБлижайший меньший элемент имеет индекс {i}, а сам элемент равняется {list_of_num[i]}.\nБлижайший больший элемент имеет индекс {j}, а сам элемент равняется {list_of_num[j]}.')

