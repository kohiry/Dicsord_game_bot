def main(count_players):
    import random
    import pprint


    users = [str(i) for i in range(1, count_players + 1)]
    not_offical_roles = ['Оборотень', 'Маньяк', 'Проститутка', 'Алкаш', 'Смертник']
    offical_roles = {}
    if 16 == count_players:
        offical_roles = {'Мирный житель': count_players - 8, 'Мафия': 3, 'Дон-мафии': 1, 'Комиссар': 1, 'Доктор': 1, 'Дополнительная роль': 2}
    elif 16 > count_players > 12:
        offical_roles = {'Мирный житель': count_players - 7, 'Мафия': 2, 'Дон-мафии': 1, 'Комиссар': 1, 'Доктор': 1, 'Дополнительная роль': 2}
    elif count_players == 12:
        offical_roles = {'Мирный житель': 5, 'Мафия': 2, 'Дон-мафии': 1, 'Комиссар': 1, 'Доктор': 1, 'Дополнительная роль': 2}
    elif 8 <= count_players < 12:
        offical_roles = {'Мирный житель': count_players - 6, 'Мафия': 1, 'Дон-мафии': 1, 'Комиссар': 1, 'Доктор': 1, 'Дополнительная роль': 1}
    else:
        print('Куда так много')
        input("Нажми любую кнопку чтобы закрыть")
        exit()
    list_keys = offical_roles.keys()
    roles_users = {}
    count_peaciful = 1
    count_add = 1
    for i in list_keys:  #бегу по списку ключей офиц ролей


        for _ in range(offical_roles[i]):  # повторяем нужное количевство данной роли
            user = random.choice(users)  # выбираем рандомного юзера на данную роль
            users.remove(user)  # удаляем данного юзера из списка обычных юзеров, чтобы не повторяться
            #нижний алгоритм образует список юзеров на опр роль
            if i == "Мирный житель":
                roles_users['Мирный-житель-' + str(count_peaciful)] = [user]
                count_peaciful += 1
            elif i == "Дополнительная роль":
                roles_users['Дополнительная-роль-' + str(count_add)] = [user]
                count_add += 1
            else:
                try:
                    roles_users[i].append(user)
                except KeyError:
                    roles_users[i] = [user]
    pprint.pprint(roles_users)
    print(not_offical_roles[0:offical_roles['Дополнительная роль']])  # даём ост юзеру доп роль
    return roles_users


if __name__ == '__main__':
        main(int(input('введи количевство игроков: '))) #наши роли main()
        input("Нажми любую кнопку чтобы закрыть")
