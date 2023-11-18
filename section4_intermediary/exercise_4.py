list_ = []

array_ = [9, 1, 8, 9, 9, 7, 2, 1, 6, 8]


def get_repeated(array_, left):
    next_ = left + 1
    while next_ < len(array_):
        next_value = array_[next_]
        left_value = array_[left]
        if (next_value == left_value):
            difference = next_ - left
            dict_ = {
                'value': next_value,
                'weight': difference
            }
            list_.append(dict_)
        next_ += 1


for index, element in enumerate(array_):
    left = index
    get_repeated(array_, left)

print(list_)

previous_weight = list_[0]["weight"]
best_case = {
    'value': 0,
    'weight': 0
}
for element in list_:
    weight = element["weight"]
    if weight < previous_weight:
        best_case['value'] = element['value']
        best_case['weight'] = weight

print(best_case)  # output: {'value': 9, 'weight': 1}
