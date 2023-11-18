list_ = []

array_ = [1, 3, 2, 2, 8, 6, 5, 9, 6, 7]


def get_repeated(array_, left):
    next_ = left + 1
    while next_ < len(array_):
        next_value = array_[next_]
        left_value = array_[left]
        if next_value == left_value:
            difference = next_ - left
            dict_ = {
                'value': next_value,
                'weight': difference
            }
            list_.append(dict_)
            if difference == 1:
                return True
        next_ += 1
    return False


for index, element in enumerate(array_):
    left = index
    if get_repeated(array_, left):
        break

print(list_)

previous_weight = list_[0]["weight"]
best_case = {
    'value': list_[0]["value"],
    'weight': list_[0]["weight"]
}
for element in list_:
    weight = element["weight"]
    if weight < previous_weight:
        best_case['value'] = element['value']
        best_case['weight'] = weight

print(best_case)  # output: {'value': 9, 'weight': 1}
