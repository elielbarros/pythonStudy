value_headquarters = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]


def get_number_best_case(list_):
    if list_:
        previous_best_case = list_[0]
        for element in list_:
            if element['difference'] < previous_best_case['difference']:
                previous_best_case = element

        return previous_best_case


def get_best_case(left_value, left, next_, array_):
    list_ = []
    while next_ < len(array_):
        if array_[next_] == left_value:
            difference = next_ - left
            best_case = {
                'left': left,
                'next_': next_,
                'left_value': left_value,
                'difference': difference
            }
            list_.append(best_case)
            if difference == 1:
                list_.clear()
                list_.append(best_case)
        next_ += 1

    return get_number_best_case(list_)


def get_all_best_case(array_):
    list_ = []
    for index, value in enumerate(array_):
        left = index
        left_value = value
        next_ = index + 1
        best_case = get_best_case(left_value, left, next_, array_)
        if best_case:
            list_.append(best_case)
    return list_


def print_best_case(array_):
    if array_:
        previous = array_[0]
        for element in array_:
            if element['difference'] < previous['difference']:
                previous = element
        print(previous)


for row_number, array_ in enumerate(value_headquarters):
    print_best_case(get_all_best_case(array_))
