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
    pass


def find_by_year(movies: list[dict], year: int) -> list[dict]:
    """Поиск всех фильмов указанного года."""
    pass
