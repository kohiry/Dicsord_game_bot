def main(count_players):
    import random
    import pprint


    users = [str(i) for i in range(1, count_players + 1)]
    not_offical_roles = ['Оборотень', 'Маньяк', 'Проститутка', 'Алкаш', 'Смертник']
    offical_roles = {}
    add_role = 2
    if count_players > 12:
        offical_roles = {'Мирный житель': count_players - 7, 'Мафия': 2, 'Дон-мафии': 1, 'Комиссар': 1, 'Доктор': 1, 'Дополнительная роль': 2}
    if count_players == 12:
        offical_roles = {'Мирный житель': 5, 'Мафия': 2, 'Дон-мафии': 1, 'Комиссар': 1, 'Доктор': 1, 'Дополнительная роль': 2}
    if count_players < 12:
        offical_roles = {'Мирный житель': count_players - 6, 'Мафия': 2, 'Дон-мафии': 1, 'Комиссар': 1, 'Доктор': 1, 'Дополнительная роль': 1}
        add_role -= 1
    list_keys = offical_roles.keys()
    roles_users = {}
    for i in list_keys:  #бегу по списку ключей офиц ролей
        for _ in range(offical_roles[i]):  # повторяем нужное количевство данной роли
            user = random.choice(users)  # выбираем рандомного юзера на данную роль
            users.remove(user)  # удаляем данного юзера из списка обычных юзеров, чтобы не повторяться
            #нижний алгоритм образует список юзеров на опр роль
            try:
                roles_users[i].append(user)
            except KeyError:
                roles_users[i] = [user]
    random.shuffle(not_offical_roles)
    print(not_offical_roles[0:add_role])  # даём ост юзеру доп роль
    pprint.pprint(roles_users)
    return roles_users


if __name__ == '__main__':
        main(int(input())) #наши роли main()
        input()
