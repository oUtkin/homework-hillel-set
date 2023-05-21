# 2. Дано: список, в якому знаходяться рядки у форматі CamelCase,
# потрібно перетворити всі рядки у формат snake_case.
#
# Приклад:
# ["FirstItem", "FriendsList", "MyTuple"]
# Результат після перетворення:
# ["first_item", "friends_list", "my_tuple"]

camelcase_list = ["FirstItem", "FriendsList", "MyTuple",]
snake_case_list = []

for i in camelcase_list:
    case_change = ''.join(['_' + j.lower() if j.isupper()
                           else j for j in i]).lstrip('_')
    snake_case_list.append(case_change)
print(snake_case_list)
