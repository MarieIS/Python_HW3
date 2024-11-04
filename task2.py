film_list = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
num = int(input('Сколько фильмов хотите добавить? '))
fav_films = []
counter = 0

while counter < num:
    film = input('Введите название вашего любимого фильма: ')
    if film in film_list:
            fav_films.append(film)
            print('Ваш любимый фильм ', film, ' добавлен в список')
    else:
            print('Этого фильма нет в списке. Попробуйте еще')
    counter += 1

print(fav_films)