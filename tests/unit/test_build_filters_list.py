import pytest

from src.infrastructure.db.postgresql.common.filters.build import _build_filters_list


@pytest.mark.parametrize(
    'filters_dict, filters_map, exclude_fields, only_fields, additional_filters, expected',
    [
        # Обычное формирование
        (
            {'test_1': 1, 'test_2': False, 'test_3': True},
            {'test_1': lambda x: x, 'test_2': lambda x: x, 'test_3': lambda x: x},
            None,
            None,
            None,
            [1, False, True],
        ),
        # Формирование с исключением полей
        (
            {'test_1': 1, 'test_2': False, 'test_3': True},
            {'test_1': lambda x: x, 'test_2': lambda x: x, 'test_3': lambda x: x},
            {'test_1'},
            None,
            None,
            [False, True],
        ),
        # Формирование конкретного фильтра
        (
            {'test_1': 1, 'test_2': False, 'test_3': True},
            {'test_1': lambda x: x, 'test_2': lambda x: x, 'test_3': lambda x: x},
            None,
            ['test_1'],
            None,
            [1],
        ),
        # Формирование фильтров с дополнительными значениями
        (
            {'test_1': 1, 'test_2': False, 'test_3': True},
            {'test_1': lambda x: x, 'test_2': lambda x: x, 'test_3': lambda x: x},
            None,
            None,
            ['test_4'],
            [1, False, True, 'test_4'],
        ),
        # Формирование фильтров с отсутствующим ключом
        (
            {'test_1': 1, 'test_2': False, 'test_3': True, 'test_4': 123},
            {'test_1': lambda x: x, 'test_2': lambda x: x, 'test_3': lambda x: x},
            None,
            None,
            None,
            [1, False, True],
        ),
        # Формирование фильтров с нулевым значением
        (
            {'test_1': 1, 'test_2': False, 'test_3': None},
            {'test_1': lambda x: x, 'test_2': lambda x: x, 'test_3': lambda x: x},
            None,
            None,
            None,
            [1, False],
        ),
        # Формирование фильтров с пустым значением
        (
            {'test_1': 1, 'test_2': False, 'test_3': ''},
            {'test_1': lambda x: x, 'test_2': lambda x: x, 'test_3': lambda x: x},
            None,
            None,
            None,
            [1, False],
        ),
    ],
)
def test_build_filters_list(
    filters_dict, filters_map, exclude_fields, only_fields, additional_filters, expected
) -> None:
    result = _build_filters_list(
        filters_dict=filters_dict,
        filters_map=filters_map,
        exclude_fields=exclude_fields,
        only_fields=only_fields,
        additional_filters=additional_filters,
    )
    for item in result:
        assert item in expected
    assert len(result) == len(expected)
