import time

shopping_list = []
available_options = 'idl'
while True:
    print('Select an option ')
    chosen_option = input('[i]nsert [d]elete [l]ist: ')

    if chosen_option == 'i':
        item_name = input('Write the item name you want to buy: ')
        shopping_list.append(item_name)
        continue
    elif chosen_option == 'd':
        if not shopping_list:
            print('Shopping list is empty')
            continue
        chosen_item_index = input('Choose the item index to delete: ')
        try:
            chosen_item_index = int(chosen_item_index)
        except:
            print('You have to choose an index to delete!')

        del shopping_list[chosen_item_index]
    elif chosen_option == 'l':
        if not shopping_list:
            print('Shopping list is empty')
            continue

        for index, item in enumerate(shopping_list):
            print(index, item)
    else:
        print('Select a valid option')
        count = 0
        while count < 3:
            time.sleep(0.5)
            print('.', end='')
            count += 1
        print('')
