def main():
    import random
    import pprint


    offical_roles = {'Мирный житель': 5, 'Мафия': 2, 'Дон мафии': 1, 'Комиссар': 1, 'Доктор': 1}
    not_offical_roles = ['Оборотень', 'Маньяк', 'Проститутка', 'Алкаш']
    users = [str(i) for i in range(1, 13)]
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
    roles_users[random.choice(not_offical_roles)] = [users[0]]  # баём ост юзеру доп роль
    pprint.pprint(roles_users) #наши роли
    return roles_users


if __name__ == '__main__':
    main()
