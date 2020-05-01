import random


offical_roles = {'Мирный житель': 4, 'Мафия': 3, 'Дон мафии': 1, 'Комиссар': 1, 'Доктор': 1}
not_offical_roles = ['Суицидник', 'Оборотень', 'Маньяк', 'Проститутка']
users = [str(i) for i in range(1, 12)]
list_keys = offical_roles.kyes()
roles_users = {}
for i in list_keys:  #бегу по списку ключей офиц ролей
    for _ in range(offical_roles[i]):  # повторяем нужное количевство данной роли
        user = random.choice(users)  # выбираем рандомного юзера на данную роль
        del users[users.index[user]]  # удаляем данного юзера из списка обычных юзеров, чтобы не повторяться
        #нижний алгоритм образует список юзеров на опр роль
        if len(roles_users[i]) == 0:
            roles_users[i] = [user]
        else:
            roles_users[i].append(user)
