import pytest
from unittest.mock import patch, Mock
from functions_for_testing_Mocks import count_elements, get_character_name, get_episodes_names


@patch('functions_for_testing_Mocks.requests')
def test_count_elements(mock_requests):
    # Создаем имитацию объекта response
    mock_response = Mock()
    # Устанавливаем возвращаемое значение для метода json
    mock_response.json.return_value = {"info": {"count": 10}}
    mock_response.ok = True
    mock_requests.get.return_value = mock_response

    status1 = 'one'
    status2 = 'two'
    status3 = 'three'

    result = count_elements(status1, status2, status3)
    # Проверяем, был ли вызван метод requests.get с ожидаемыми аргументами
    mock_requests.get.assert_called_once_with(
        url="https://qwerty/",
        params={'status1': status1, 'status2': status2, 'status3': status3}
    )
    # Проверяем, соответствует ли возвращенный результат ожидаемому значению
    assert result == 10


@patch('functions_for_testing_Mocks.requests.get')
def test_get_character_name(mock_get):
    mock_response = mock_get.return_value
    mock_response.ok = True
    mock_response.json.return_value = {"name": "Morty"}
    result = get_character_name()
    assert result == "Morty"


@patch('functions_for_testing_Mocks.requests.get')
def test_get_episodes_names(mock_get):
    mock_response = mock_get.return_value
    mock_response.ok = True
    mock_response.json.return_value = [
        {"name": "episode 1"},
        {"name": "episode 2"}
    ]
    result = get_episodes_names()
    assert result == ["episode 1", "episode 2"]
