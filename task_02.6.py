goods = []
features = {'Наименование': '', 'Цена': '', 'Количество': '', 'Ед.изм': ''}
analytics = {'Наименование': [], 'Цена': [], 'Количество': [], 'Ед.изм': []}
num = 0
feature_ = None
control = None
while True:
    control = input("Для выхода нажмите ' Q ', для продолжения нажмите 'Enter', для аналитики нажмите 'A'.").upper()
    if control == 'Q':
        break
    num += 1
    if control == 'A':
        print(f'\n Текущая аналитика \n {"-" * 30}')
        for key, value in analytics.items():
            print(f'{key[:25]:>30}: {value}')
            print("-" * 30)
    for f in features.keys():
        feature_ = input(f'Input feature "{f}"')
        features[f] = int(feature_) if (f == 'price' or f == 'quantity') else feature_
        analytics[f].append(features[f])
    goods.append((num, features))
