import pytest
from unittest.mock import patch, Mock
from number_of_characters import count_elements


@patch('number_of_characters.requests')
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
