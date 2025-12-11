from logic import load_movies, save_movies, add_movie, mark_watched, find_by_year

DATA_FILE = "movies.json"


def main():
    movies = load_movies(DATA_FILE)

    while True:
        print("\nКаталог фильмов")
        print("1. Показать все фильмы📽️")
        print("2. Добавить фильм➕")
        print("3. Отметить фильм как просмотренный(❁´◡`❁)")
        print("4. Найти фильмы по году🔎")
        print("0. Выход🏁")

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


def show_all_movies(movies):
    """Показывает все фильмы."""
    if not movies:
        print("Список фильмов пуст.")
        return

    print("\nВсе фильмы:")
    print("-" * 50)
    for movie in movies:
        status = "Просмотрено |" if movie.get('watched', False) else "Не просмотрено |"
        print(f"{status} [{movie['id']}] {movie['title']} ({movie['year']})")


def add_movie_menu(movies):
    """Меню добавления фильма."""
    title = input("Название фильма: ").strip()
    if not title:
        print("Название не может быть пустым.")
        return movies

    while True:
        try:
            year = int(input("Год выпуска: ").strip())
            if year > 0:
                break
            print("Год должен быть положительным.")
        except ValueError:
            print("Введите корректный год (число).")

    movies = add_movie(movies, title, year)
    print(f"Фильм '{title} ({year})' добавлен!")
    return movies


def mark_watched_menu(movies):
    if not movies:
        print("Список пуст.")
        return movies

    show_all_movies(movies)  # показываем для выбора

    while True:
        try:
            movie_id = int(input("ID фильма: ").strip())
            found = False
            for movie in movies:
                if movie.get('id') == movie_id:
                    movie['watched'] = True
                    found = True
                    print("Готово!")
                    break
            if not found:
                print("Фильм с таким ID не найден.")
            return movies
        except ValueError:
            print("Введите корректный ID (число).")


def find_by_year_menu(movies):
    while True:
        try:
            year = int(input("Год: ").strip())
            found_movies = find_by_year(movies, year)

            if found_movies:
                print(f"\nФильмы {year} года:")
                print("-" * 50)
                for movie in found_movies:
                    status = "Просмотрено" if movie.get('watched', False) else "Не просмотрено"
                    print(f"{status} [{movie['id']}] {movie['title']}")
            else:
                print(f"Фильмов {year} года не найдено.")
            return
        except ValueError:
            print("Введите корректный год (число).")


if __name__ == "__main__":
    main()
