from logic import load_movies, save_movies, add_movie, mark_watched, find_by_year, show_all_movies, add_movie_menu, \
    mark_watched_menu, find_by_year_menu

DATA_FILE = "movies.json"


def main():
    movies = load_movies(DATA_FILE)

    while True:
        print("\nКаталог фильмов")
        print("1. Показать все фильмы📽️")
        print("2. Добавить фильм➕")
        print("3. Отметить фильм как просмотренный")
        print("4. Найти фильмы по году🔎")
        print("0. Выход")

        choice = input("Выберите пункт: ")

        if choice == "1":
            show_all_movies(movies)

        elif choice == "2":
            movies = add_movie_menu(movies)

        elif choice == "3":
            movies = mark_watched_menu(movies)

        elif choice == "4":
            find_by_year_menu(movies)

        elif choice == "0":
            save_movies(DATA_FILE, movies)
            print("Гуд бай америка!")
            break

        else:
            print("Неверный пункт меню.")

if __name__ == "__main__":
    main()
