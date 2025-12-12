import json


def load_movies(path: str) -> list[dict]:
    """Загрузка списка фильмов из JSON-файла."""
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_movies(path: str, movies: list[dict]) -> None:
    """Сохранение списка фильмов в JSON-файл."""
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(movies, f, ensure_ascii=False, indent=4)


def add_movie(movies: list[dict], title: str, year: int) -> list[dict]:
    """Добавление нового фильма в список."""
    if movies:
        max_id = max(movie['id'] for movie in movies)
    else:
        max_id = 0
    new_movie = {
        "id": max_id + 1,
        "title": title,
        "year": year,
        "watched": False
    }
    return movies + [new_movie]


def mark_watched(movies: list[dict], movie_id: int) -> list[dict]:
    """Отметить фильм как просмотренный."""
    for movie in movies:
        if movie.get('id') == movie_id:
            movie['watched'] = True
            break
    return movies


def find_by_year(movies: list[dict], year: int) -> list[dict]:
    """Поиск всех фильмов указанного года."""
    return [movie for movie in movies if movie.get('year') == year]

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