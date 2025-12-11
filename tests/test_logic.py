import pytest
import json
from logic import load_movies, save_movies, add_movie, mark_watched


def test_load_movies(tmp_path):
    test_data = [{"id": 1, "title": "Test", "year": 2020, "watched": False}]
    path = tmp_path / "movies.json"
    path.write_text(json.dumps(test_data))

    result = load_movies(str(path))
    assert result == test_data


def test_save_movies(tmp_path):
    movies = [{"id": 1, "title": "Test", "year": 2020, "watched": False}]
    path = tmp_path / "movies.json"

    save_movies(str(path), movies)

    result = json.loads(path.read_text())
    assert result == movies


def test_add_movie():
    movies = [{"id": 1, "title": "Old", "year": 2019, "watched": False}]
    result = add_movie(movies, "New", 2020)
    assert len(result) == 2
    assert result[1]["title"] == "New"
    assert result[1]["id"] == 2


def test_mark_watched():
    movies = [{"id": 1, "title": "Test", "year": 2020, "watched": False}]
    result = mark_watched(movies, 1)
    assert result[0]["watched"] == True
